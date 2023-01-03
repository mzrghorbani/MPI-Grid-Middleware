from DIRAC.Core.Base import Script as Script
Script.parseCommandLine(ignoreErrors=False)
from DIRAC.Interfaces.API.Job import Job
from DIRAC.Interfaces.API.Dirac import Dirac
dirac = Dirac()
j = Job()
j.setName('API-20-09-2022')
j.setCPUTime(500)
j.setExecutable('cp', arguments='input.txt output.txt', logFile='log.log')
j.setInputData('/gridpp/user/m/maziar.ghorbani/mydata/test/input.txt')
j.setOutputSandbox('output.txt')
j.setOutputData(['my_data.copy'])
jobID = dirac.submitJob(j)
print('Submission Result: ', jobID)
