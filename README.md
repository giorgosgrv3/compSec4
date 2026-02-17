The contents are:

-- venv : includes fabric and paramiko, used to run the tests, otherwise they won't run.
-- test.py : the ssh test we run on localhost, that uses paramiko through fabric, and eventually calls the quine channel.py inside the paramiko directory in the venv.
--find_paths.py : point us to the installation of fabric and paramiko in the venv

--test.yara : contains our yara rule

-- ossec_log.txt : contains proof from inside the OSSEC log, that the modifications in channel.py were caught by OSSEC
-- yara_log.txt : contains proof that Yara caught the key string "PWNED" inside channel.py of BOTH the original paramiko folder, as well as the dummy folder paramiko_clone we used for the quine to infect.

Our modification/quine in the paramiko folder can either be seen in venv/...../paramiko/channel.py, or in the dummy
paramiko directory paramiko_clone/channel.py, which has already been infected by the quine from our tests.