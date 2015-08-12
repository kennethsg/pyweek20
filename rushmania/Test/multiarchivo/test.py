import perro
import dueno


dog = perro.Perro()
owner = dueno.Dueno()
owner.dog = dog

'''
def cambiar_nombre():
    dog.name = "Canela"
'''
#otroarchivo.Otro_Archivo().cambiar_nombre()
print(dog.name)


def main():
    owner.cambiar_nombre()
    print(dog.name)
    '''
    x = 20
    
    def cambiar_x(x):
        x = 500
    
    cambiar_x(x)
    print(x)
    '''

if __name__ == "__main__":
    main()