#pre-installations
#sudo apt update
#sudo apt install nfs-kernel-server
#mkdir /temp/shared
#vim /etc/exports
#/home/user/cluster_shared IP_CLIENT1(rw,no_subtree_check) IP_CLIENT2(rw,no_subtree_check) IP_CLIENT3(rw,no_subtree_check)
#exportfs -ra
#sudo ufw allow from IP_CLIENT1 to any port nfs
#sudo ufw allow from IP_CLIENT2 to any port nfs
#sudo ufw status
#sudo apt update
#sudp apt install nfs-common
#mkdir -p /temp/shared
#mount IP_HOST:/temp/shared /temp/shared
#vim /etc/fstab
#IP_HOST:/temp/shared /temp/shared nfs defaults 0 0
#cd pool_shared
#touch node1.txt node2.txt node3.txt

#automatic install of packages if they are not installed already
list.of.packages <- c(
  "foreach",
  "doParallel",
  "ranger"
  )

new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]

if(length(new.packages) > 0){
  install.packages(new.packages, dep=TRUE)
}

#loading packages
for(package.i in list.of.packages){
  suppressPackageStartupMessages(
    library(
      package.i, 
      character.only = TRUE
      )
    )
}

#creating the input folder
input.folder <- "/temp/shared"
dir.create(input.folder)

#data frame names
df.names <- paste0("y", 1:100)

#filling it with files
for(i in df.names){
  
  #creating the df
  df.i <- data.frame(
    y = rnorm(1000),
    a = rnorm(1000),
    b = rnorm(1000),
    c = rnorm(1000),
    d = rnorm(1000)
  )
  
  #changing name of the response variable
  colnames(df.i)[1] <- i
  
  #assign to a variable with name i
  assign(i, df.i)
  
  #saving the object
  save(
    list = i,
    file = paste0(input.folder, "/", i, ".RData")
  )
  
  #removing the generated data frame form the environment
  rm(list = i, df.i, i)
  
}

#generate pool specification
spec <- pool_spec(
  ips = c('10.42.0.1', '10.42.0.34', '10.42.0.104'),
  cores = c(7, 4, 4),
  user = "mghorbani"
)

#define parallel port
Sys.setenv(R_PARALLEL_PORT = 11000)
Sys.getenv("R_PARALLEL_PORT")

#setting up pool
my.pool <- parallel::makepool(
  master = '10.42.0.1', 
  spec = spec,
  port = Sys.getenv("R_PARALLEL_PORT"),
  outfile = "",
  homogeneous = TRUE
)

#check pool definition (optional)
print(my.pool)

#register pool
doParallel::registerDoParallel(cl = my.pool)

#check number of worker nodes
foreach::getDoParWorkers()

#list of input files as iterator
input.files <- list.files(
  path = input.folder,
  full.names = FALSE
)

modelling.summary <- foreach(
  input.file = input.files,
  .combine = 'rbind', 
  .packages = "ranger"
) %dopar% {
  
  # 1. input file name without extension
  input.file.name <- tools::file_path_sans_ext(input.file)
  
  # 2. read input file
  df <- get(load(paste0(input.folder, "/", input.file)))
  
  # 3. fit model
  m.i <- ranger::ranger(
    data = df,
    dependent.variable.name = colnames(df)[1],
    importance = "permutation"
  )
  
  # 4. change name of the model to one of the response variable
  assign(input.file.name, m.i)
  
  # 5. save model
  save(
    list = input.file.name,
    file = paste0(output.folder, "/", input.file)
  )
  
  # 6. returning summary
  return(
    data.frame(
      response.variable = input.file.name,
      r.squared = m.i$r.squared,
      importance.a = m.i$variable.importance["a"],
      importance.b = m.i$variable.importance["b"],
      importance.c = m.i$variable.importance["c"],
      importance.d = m.i$variable.importance["d"]
    )
  ) 
}

# Termonate process
parallel::stoppool(cl = my.pool)
