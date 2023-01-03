from DIRAC.Core.Base import Script as Script
Script.parseCommandLine(ignoreErrors=False)
from DIRAC.Interfaces.API.Dirac import Dirac
from DIRAC.Interfaces.API.Job import Job
import sys
dirac = Dirac()
jobid = sys.argv[1]
print("----------Get Job Summary----------")
print(dirac.getJobSummary(jobid))
print("----------Get Job Parameters----------")
print(dirac.getJobParameters(jobid))
print("----------Get Job Status----------")
print(dirac.getJobStatus(jobid))
