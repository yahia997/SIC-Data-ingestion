import sys
import shutil
import time
import socket
import signal

if _name_ == "_main_":
  if len(sys.argv) < 1:
    print >> sys.stderr, "Usage: spool_stream.py <spool_dir> <lines> <files> "
    exit(-1)

  sleeptime = float(5)
  spool_dir = sys.argv[1]
  N = int(sys.argv[2])
  filelist = sys.argv[3:]
  
  def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    infile.close()
    w_file.close()
    sys.exit(0)

  signal.signal(signal.SIGINT, signal_handler)
  print 'Press Ctrl+C'
  
  fileN = 0

  while True:
    for filename in filelist:
      infile = open(filename, 'r')
      while True:
        lines = infile.read(N)
        if not lines:
          break
        else:
          fname = str(fileN) + ".txt"
          tname = "/tmp/" + fname
          sname = spool_dir + "/" + fname
          fileN += 1
          w_file = open(tname, "w")
          w_file.write(lines)
          w_file.close()
          shutil.move(tname, sname)
        time.sleep(sleeptime)
