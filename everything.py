"Indexes everything, so I don't have to."
import pathlib

current_dir = pathlib.Path(__file__).parent

output_file_path = current_dir.joinpath('everything.txt')
output_file_path.touch()

stuff_things = {}

for stuff_thing in current_dir.iterdir():
  if stuff_thing.is_dir():
    # only goes one level deep (that's partly why I recommend using Github to see everything)
    stuff_thing_stuff_things = []
    for stuff_thing_stuff_thing in stuff_thing.iterdir():
      stuff_thing_stuff_things.append(stuff_thing_stuff_thing.name)
    stuff_things.update({stuff_thing.name: stuff_thing_stuff_things})
  else:
    stuff_things.update({stuff_thing.name: None})

# write it out
#  write it out
#   write it out

lines = ['This file shows (probably) everything in this website. I recommend you instead look at the source code at https://github.com/nicodoggy/nicodoggy\n\n']

for stuff_thing in stuff_things:
  if type(stuff_things[stuff_thing]) == list:
    lines.append(f'├── {stuff_thing}\n')
    for stuff_thing_stuff_thing in stuff_things[stuff_thing]:
      lines.append(f'│   ├── {stuff_thing_stuff_thing}\n')
  else:
    lines.append(f'├── {stuff_thing}\n')

with open(output_file_path, 'w') as output_file:
  output_file.writelines(lines)
