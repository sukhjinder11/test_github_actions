import sys

print('Hello from Python Script')
pr_type = sys.argv[1]
current_release = sys.argv[2]

print('current release: ' + current_release)
cur_rel = current_release.split('v')[1].split('.')

if pr_type == 'bug':
    i = 2
elif pr_type == 'enhancement':
    i = 1
elif pr_type == 'major':
    i = 0

n = cur_rel[i]
n = str(int(n) + 1)
cur_rel[i] = n

next_release = 'v' + cur_rel[0] + '.' + cur_rel[1] + '.' + cur_rel[2]
print('next_release: ' + next_release)



