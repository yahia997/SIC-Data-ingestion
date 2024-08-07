# this file generates random codeforces submition logs
import datetime
import random
languages = ["java", "python", "c++", "javascript", "c", "c#"]
problems = "ABCDEFGHIJKLMNOPQRSTUVWYXZ"
ContestID = ["1", "2", "3", "4", "5", "6"]
stats = ["Accepted", "Time Limit Exceeded", "Wrong Answer"]

# SubmissionID,
# ProblemID,
# ContestID,
# ProgrammingLanguage,
# Time,
# Memory,
# TestCase,
# SubmissionTime


f =  open('./logs.txt', mode='a')

for i in range(100000):

  # SubmissionID
  f.write("{v},".format(v=random.randint(0, 1000000)))
  # # ProblemID
  f.write("{v},".format(v=random.choice(problems)))
  # # ContestID
  f.write("{v},".format(v=random.randint(0, 1000000)))
  # # ProgrammingLanguage
  f.write("{v},".format(v=random.choice(languages)))
  # # Time
  f.write("{v} ms,".format(v=random.randint(0, 2000)))
  # # Memory
  f.write("{v} KB,".format(v=random.randint(0, 2000000000)))
  # # TestCase
  f.write("{v},".format(v=random.choice(stats)))
  # # SubmissionTime
  f.write("{v}".format(v=datetime.datetime(random.randint(2010, 2024), random.randint(1, 12), random.randint(1, 28), random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))))

  f.write("\n")

f.close()