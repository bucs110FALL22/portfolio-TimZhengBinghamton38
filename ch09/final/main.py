import techyproxy
import fakenameproxy

def main():
    techapi = techyproxy.Techyquoteapi()
    fakeapi = fakenameproxy.Fakenameapi()
    quote = techapi.get()
    name = fakeapi.get()
    print(name)
    city = fakeapi.get_location()
    print(city)
    # personsaid = name + " says:"
    # print(personsaid)
    # newquote = '"' + quote + '"'
    # print(newquote)

main()