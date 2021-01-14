import os
import re

DATA_DIR = "/home/jack/Data/maildir"
OUT_FILE = "/home/jack/Data/enron_out.csv"

outfile = open(OUT_FILE, 'w')

def parse_sent_mail():
  def parse_files_from_dir(dir):
    if os.path.isdir(dir):
      files = os.listdir(dir)
      for file in files:
        with open(dir + file, 'r') as f:
          outlook = False
          forwarded = False
          if outlook:
            # do outlook things
            print("what")
          elif forwarded:
            # do forwarded things
            print("what what")
          else:
            lines = f.readlines()
            for line in range(len(lines)):
              pat = re.compile("X-FileName")
              if re.search(pat, lines[line]) and line + 2 < len(lines):
                msg = " ".join(lines[line + 2:]).replace('\t', ' ').replace('\n', ' ')
                outfile.write(msg + '\n');


  for dirnames in os.listdir(DATA_DIR):
    parse_files_from_dir(DATA_DIR + '/' + dirnames + '/_sent_mail/')
    parse_files_from_dir(DATA_DIR + '/' + dirnames + '/sent_items/')
    parse_files_from_dir(DATA_DIR + '/' + dirnames + '/sent/')
    break


parse_sent_mail()

outfile.close()