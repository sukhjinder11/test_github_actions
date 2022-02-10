import sys

print('Hello from Python Script')
pr_type = sys.argv[1]
current_release = sys.argv[2]

print('current release: ' + current_release)
cur_rel = current_release.split('v')[1].split('.')

if pr_type == 'bug':
    cur_rel[2] = 'bug'


next_release = 'v' + cur_rel[0] + '.' + cur_rel[1] + '.' + cur_rel[2]




