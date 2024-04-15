import os

def split_file(input_file, output_folder, lines_per_file=1000000):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(input_file, 'r') as f:
        count = 0
        part_num = 1
        out_file = None

        for line in f:
            if count % lines_per_file == 0:
                if out_file:
                    out_file.close()
                out_file = open(os.path.join(output_folder, f'{part_num}.txt'), 'w')
                part_num += 1
            out_file.write(line)
            count += 1

        if out_file:
            out_file.close()

def getIntSafe():
  try:
      return int(input("Lines per file, default = 1000000: "))
    except ValueError:
      return 1000000

if __name__ == '__main__':
  fname = input("File name to split: ")
  count_lines_per_chunk = getIntSafe()
  out_folder = input("Output folder to save chunks: ")
  split_file(fname, out_folder, count_lines_per_chunk)
