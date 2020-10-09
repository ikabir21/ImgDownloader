from requests import get

with open(input('ENTER FILE NAME: '),'wb') as f:
    
    f.write(get(input("ENTER THE LINK: ")).content)

print("\nFILE DOWNLOADED!")