def replace_file(pattern, replace, file1, file2):
     try:
          fin = open(file1 ,'r')
          fout = open(file2, 'w')

          for line in fin:
               line = line.replace(pattern, replace)
               fout.write(line)

          fin.close()
          fout.close()
     except:
          print('error!!')
     finally:
          print('------')



def main():
     pattern = 'pattern'
     replace = 'replace'
     source = 'text.txt'
     dest = 'replaced_' + source
     replace_file(pattern, replace, source, dest)


if __name__ == '__main__':     
     main()
