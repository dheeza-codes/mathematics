from rectangle import Rectangle
from square import Square
from circle import Circle
from triangle import Triangle
def main():
        print("Calculate Area")
        print("1. square")
        print("2. rectangle")
        print("3. circle")
        print("4. triangle")
        choice = int(input("Enter your choice: "))
        
        if choice == 1: 
             side = float(input("Enter square sides length: "))
             square_area = Square(side)
             print(square_area.get_area())

        
        elif choice == 2:
            length = float(input("Enter rectangle length: "))
            breath = float(input("Enter rectangle breath: "))
            rectangle_area =Rectangle(length, breath)
            print(rectangle_area.get_area())
        
                
        elif choice == 3:
            radius = float(input("Enter circle radius: "))
            circle_area = Circle(radius)
            print(circle_area.get_area())
            
        elif choice == 4:
            base = float(input("Enter triangle base: "))
            height = float(input("Enter triangle height: "))
            triangle_area = Triangle(base, height)
            print(triangle_area.get_area())
            
            
        else:
            print("invalid option")
            
main()