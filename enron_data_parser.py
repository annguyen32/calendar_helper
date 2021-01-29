import os
import re

DATA_DIR = "/home/jack/Data/maildir"
OUT_FILE = "/home/jack/Data/enron_out.csv"

outfile = open(OUT_FILE, 'w')

def parse_sent_mail():
  # get rid of useless junk
  stop_words = [r"\*{70}.+\*{70}", r"This message (including any attachments) contains confidential information  intended for a specific individual and purpose, and is protected by law.  If  you are not the intended recipient, you should delete this message and are  hereby notified that any disclosure, copying, or distribution of this  message, or the taking of any action based on it, is strictly prohibited."]
  split_words = [r"-----Original Message-----.+Subject:"]
  # Killing forwarded message loses subject data
  stop_msgs = [r"---------------------------------- Forwarded.+---------------------------"]
  def parse_files_from_dir(dir):
    def strip_whitespace(words):
      return re.sub(re.compile('\s+'), ' ', words)

    def strip_stopwords(words):
      for sw in stop_words:
        pat = re.compile(sw)
        words = re.sub(pat, '', words)
      return words

    def split_messages(words):
      for w in split_words:
        pat = re.compile(w)
        words = re.sub(pat, '\n', words)
      return words


    if os.path.isdir(dir):
      files = os.listdir(dir)
      for file in files:
        with open(dir + file, 'r') as f:
          outlook = False
          if outlook:
            # do outlook things
            print("do outlook things")
          else:
            lines = f.readlines()
            foundXFile = False
            msg = ''
            for line in range(len(lines)):
              pat = re.compile("X-FileName")
              if re.search(pat, lines[line]) and line + 2 < len(lines):
                msg = " ".join(lines[line + 2:])
                foundXFile = True
                break
            if not foundXFile:
              msg = " ".join(lines)
            
            forwarded = False
            for sm in stop_msgs:
              pat = re.compile(sm)
              forwarded = re.search(pat, msg) or forwarded

            if not forwarded:
              msg = strip_whitespace(msg)
              msg = strip_stopwords(msg)
              msg = split_messages(msg)
              outfile.write(msg + '\n');


  for dirnames in os.listdir(DATA_DIR):
    parse_files_from_dir(DATA_DIR + '/' + dirnames + '/_sent_mail/')
    parse_files_from_dir(DATA_DIR + '/' + dirnames + '/sent_items/')
    parse_files_from_dir(DATA_DIR + '/' + dirnames + '/sent/')
    break


parse_sent_mail()

outfile.close()