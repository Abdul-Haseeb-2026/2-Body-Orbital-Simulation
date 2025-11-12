#Orbital Simulation meant to represent orbits like the Earth and Moon's orbit. Will be used to compare accuracry of different numerical integrators
#Integrators in this version:
#-----Euler Integrator
#-----Velocity Verlet Integrator

#Next Integrator:
#------Runge Kutta (Yes I know it sounds funny)




from unicodedata import numeric
import pygame
from sys import exit
import math
from pygame.locals import K_BACKSPACE

global integrator
global mass_inp, MASS_inp, velocity_inp
global index
global inp_list, surf_list
global G
G =  6.6743 * (10 ** (-11))
# globalising variables
global mass_inp_rect, vel_inp_rect, MASS_inp_rect

pygame.init()

pixel = 1500000 # 1 pixel = 1,500,000 metres



# Design dimensions
design_height = 700
design_width = 700

# fonts
bigfont = pygame.font.Font(None, 72)
midfont = pygame.font.Font(None, 54)
smallfont = pygame.font.Font(None, 36)
tinyfont = pygame.font.Font(None, 20)






# title text
Two_D = bigfont.render("2D", True, 'Blue')     #2D
Text1 = bigfont.render("Physics", True, 'White')    #Physics
Text2 = bigfont.render("Engine", True, 'White') #Engine
# options
Opt1 = midfont.render("Euler Integrator", True, '#203531')  #Option 1: An Euler Integrator Based Simulation 
Opt2 = midfont.render("Velocity Verlet", True, '#352024')    #Option2: A Velocity Verlet Based Simulation
# Title rectangles
Two_D_rect = Two_D.get_rect(center=(design_width // 2, 100))
Text1_rect = Text1.get_rect(center=(design_width // 2, 150))        #making rectangle for each surface created for the title screen
Text2_rect = Text2.get_rect(center=(design_width // 2, 200))

Opt1_rect = Opt1.get_rect(center=(design_width // 2, 350))          
Opt2_rect = Opt2.get_rect(center=(design_width // 2, 450))



# sidebar
side_back = pygame.Surface((design_width // 2, 500))
side_back.fill("#3E4B4F")

velocity = smallfont.render("Velocity  = ", True, "White")
mass = smallfont.render("mass = ", True, "White")
MASS = smallfont.render("MASS  = ", True, "White")

exit_text = smallfont.render(" EXIT ", True, "White")
start_text = smallfont.render(" START ", True, "White")
pause_text = smallfont.render(" PAUSE ", True, "White")
info_text = smallfont.render(" (i) ", True, "White")

velocity_inp = pygame.Surface((100, 50))
velocity_inp.fill("Blue")

mass_inp = pygame.Surface((100, 50))
mass_inp.fill("Blue")

MASS_inp = pygame.Surface((100, 50))
MASS_inp.fill("Blue")

# sidebar rectangles
mass_rect = mass.get_rect(midleft=(380, 300))
velocity_rect = velocity.get_rect(midleft=(380, 400))
MASS_rect = MASS.get_rect(midleft=(380, 500))

exit_rect = exit_text.get_rect(bottomleft=(design_width // 2, 250))
start_rect = start_text.get_rect(bottomleft=(450, 250))
pause_rect = pause_text.get_rect(topleft=(0, 0))
info_rect = info_text.get_rect(topright=(700, 0))

mass_inp_rect = mass.get_rect(midleft=(mass_rect.right + 5, 300))
velocity_inp_rect = velocity.get_rect(midleft=(velocity_rect.right + 5, 400))
MASS_inp_rect = MASS.get_rect(midleft=(MASS_rect.right + 5, 500))


#Collision popup screen Surfaces and rects


Col_Text = bigfont.render("Collision occured", True, "#B41515D3")    
Home_Button = bigfont.render("Home", True, 'White')

Col_Text_rect = Col_Text.get_rect(center=(350, 350))
Home_Button_rect = Home_Button.get_rect(center=(350, 450))


# initializing display screen
screen = pygame.display.set_mode((design_width, design_height))

def Show_Orbit(): # Function to show the screen to input data on the orbits
    pygame.draw.rect(screen, "Red", exit_rect)
    
    screen.blit(side_back, (350, 250))
    screen.blit(MASS, MASS_rect)
    screen.blit(mass, mass_rect)
    screen.blit(velocity, velocity_rect)
    
    screen.blit(exit_text, exit_rect)
    screen.blit(start_text, start_rect)
    
    

    screen.blit(MASS_inp, MASS_inp_rect)
    screen.blit(mass_inp, mass_inp_rect)
    screen.blit(velocity_inp, velocity_inp_rect)

def show_homescreen(): # Function to show the screen to select the desired simulation (Orbital simulation only available currently)
    screen.blit(Two_D, Two_D_rect)
    screen.blit(Text1, Text1_rect)
    screen.blit(Text2, Text2_rect)

    pygame.draw.rect(screen, "#FDE71F", Opt1_rect)
    pygame.draw.rect(screen, "#FA1580", Opt2_rect)

    screen.blit(Opt1, Opt1_rect)
    screen.blit(Opt2, Opt2_rect)

def Collision_popup(): #Displaying Popup in case of Collision
    #screen.blit(Popup_Surf,Popup_Surf_rect)
    pygame.draw.rect(screen, "#36C5B2", Home_Button_rect)
    screen.blit(Col_Text,Col_Text_rect)    
    screen.blit(Home_Button,Home_Button_rect) 

    
        


# showing text inputs
index = 0
mass_val = ""
MASS_val = ""
velocity_val = ""
def text_output(mass_val, MASS_val, velocity_val): # This will get inputs, adjust the coloured boxes behind the text being insterted, highlight any input box being used to input data and output to the user
    global mass_inp_rect, vel_inp_rect, MASS_inp_rect
    global mass_inp, MASS_inp, velocity_inp
    global index
    global inp_list, surf_list

    mass_str = smallfont.render(mass_val, True, "White")
    mass_str_rect = mass_str.get_rect(midleft=(mass_inp_rect.left + 5, 300))
    velocity_str = smallfont.render(velocity_val, True, "White")
    velocity_str_rect = velocity_str.get_rect(midleft=(velocity_inp_rect.left + 5, 400))
    MASS_str = smallfont.render(MASS_val, True, "White")
    MASS_str_rect = MASS_str.get_rect(midleft=(MASS_inp_rect.left + 5, 500))

    if mass_str_rect.right >= mass_inp_rect.right:
        width = mass_str.get_width() + 10
        mass_inp_rect.w = width
    mass_inp = pygame.Surface((mass_inp_rect.w, 50))

    if MASS_str_rect.right >= MASS_inp_rect.right:
        width = MASS_str.get_width() + 10
        MASS_inp_rect.w = width
    MASS_inp = pygame.Surface((MASS_inp_rect.w, 50))

    if velocity_str_rect.right >= velocity_inp_rect.right:
        width = velocity_str.get_width() + 10
        velocity_inp_rect.w = width
    velocity_inp = pygame.Surface((velocity_inp_rect.w, 50))

    inp_list = [mass_inp_rect, MASS_inp_rect, velocity_inp_rect]
    surf_list = [mass_inp, MASS_inp, velocity_inp]

    for rect, surf in zip(inp_list, surf_list):
        surf.fill("Blue")
        if rect.collidepoint(pos) and pygame.mouse.get_pressed():
            bord_rect = rect.copy()
            bord_rect.inflate_ip(10, 10)
            surf.fill("Green")
            pygame.draw.rect(side_back, "Red", bord_rect, 5)

    screen.blit(mass_inp, mass_inp_rect)
    screen.blit(mass_str, mass_inp_rect)
    screen.blit(MASS_inp, MASS_inp_rect)
    screen.blit(MASS_str, MASS_inp_rect)
    screen.blit(velocity_inp, velocity_inp_rect)
    screen.blit(velocity_str, velocity_inp_rect)
    return index, inp_list, surf_list

def y(n):
    return design_height - n

def get_d(pos, center): # Get distance between the two bodies
    P = pos[0] - center[0]
    O = pos[1] - center[1]
    d = (math.sqrt((P ** 2) + (O ** 2)))
    angle = math.atan2(O, P)
    return angle, float(d)

def get_Force(d, mass_val, MASS_val): # Get Gravitational Force between the two bodies
    G = 6.6743 * (10 ** (-11))
    Force = G * float(mass_val) * float(MASS_val)
    return Force / (d ** 2)

def get_acc(F, M, d, angle):  # Get acceleration of the body due to the force on them.It is negative due to the force being attractive
    
    a = F/M
    
    return -a

def get_v(ax, ay, vx, vy, dt):  # Gets vector components for total net velocity of a body
    vx = (0.5 * ax * dt) + vx
    vy = (0.5 * ay * dt) + vy
    return vx, vy


# classes

class CenterBody:    #  A class to make an object that acts as the central body
    def __init__(self,m,pix):
        self.angle = 0  #angle initialized so it can be updated outside of class
        self.mass = m
        self.pos = (350*pix,350*pix)
        self.vx,self.vy = 0,0
    def updatepos(self,dt,innitialisation,m,Force,mass_pos):
        if integrator == "Velocity":
            self.Force = -Force
            if innitialisation == False: # ensures necessary initial values are input if not initialised already
                self.angle,self.dist = get_d(self.pos, mass_pos)   
                self.a = get_acc(self.Force,self.mass,self.dist,self.angle)
                self.ax = self.a * math.cos(self.angle)
                self.ay = self.a * math.sin(self.angle)
            innitialisation = True

            #  Applying Velocity Verlet Integration
            self.new_dx = (self.vx*dt) + 0.5*self.ax*dt*dt  
            self.new_dy = (self.vy*dt) + 0.5*self.ay*dt*dt
            
            self.pos =(self.pos[0] + self.new_dx ,self.pos[1])
            self.pos =(self.pos[0]  ,self.pos[1] + self.new_dy)

            
            self.angle,self.dist = get_d(self.pos, mass_pos)
            self.new_Force = get_Force(self.dist,self.mass,m)
            self.new_a = -self.new_Force/self.mass
            self.new_ax = self.new_a * math.cos(self.angle)
            self.new_ay = self.new_a * math.sin(self.angle)
            self.new_vx = self.vx + 0.5*(self.ax + self.new_ax) *dt
            self.new_vy = self.vy + 0.5*(self.ay + self.new_ay) *dt
            self.vx,self.vy = self.new_vx,self.new_vy
            self.ax,self.ay = self.new_ax,self.new_ay
       

        elif integrator == "Euler":
            if innitialisation ==  False:
                self.dx,self.dy = 0,0
            self.angle,self.dist = get_d(self.pos, mass_pos)
            self.Force = Force
            self.a = get_acc(self.Force,self.mass,self.dist,self.angle)#Getting acceleration after time dt
            self.ax = self.a * math.cos(self.angle) 
            self.ay = self.a * math.sin(self.angle)    #Getting vector components of acceleration
            self.vx = self.vx + self.ax*dt     #Getting vector components of velocity after time dt
            self.vy = self.vy + self.ay*dt
            self.dx = self.vx*dt     #Getting vector components of change in displacement after time dt
            self.dy = self.vy*dt
            self.pos = [self.pos[0] + self.dx,self.pos[1]]       #changing position of central mass 
            self.pos = [self.pos[0] ,self.pos[1] + self.dy]

        self.v = ((self.vx*self.vx) + (self.vy*self.vy))**0.5
        #Updating energy of the central mass only

        self.energy =  0.5*self.mass*self.v*self.v

black = pygame.Surface((design_width, design_height))#Background colour initialisation
black.fill('Black')


mass_active = False
MASS_active = False         # Boolean Flags to point out whether a input box is actively being pressed
velocity_active = False
pause = False  # Flag to show whether game is in pause state or not
active = [mass_active, MASS_active, velocity_active]

index = 0

state = "home"# Initialising state to be home

# -------------------------------MAIN LOOP---------------------------------------
while True:
    clock = pygame.time.Clock()
    pos = pygame.mouse.get_pos()  # Getting position if mouse 
    for event in pygame.event.get(): # Event loop 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and Opt2_rect.collidepoint(pos): # if mouse button clicked on Option 2(which is Orbit)
            state = "setup orbit"
            integrator = "Velocity"
        if event.type == pygame.MOUSEBUTTONDOWN and Opt1_rect.collidepoint(pos): # if mouse button clicked on Option 2(which is Orbit)
            state = "setup orbit"
            integrator = "Euler"

        if state == "setup orbit":
            if mass_inp_rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                mass_active = True
                MASS_active = False
                velocity_active = False
            if event.type == pygame.KEYDOWN and mass_active:   # Getting text input/being deleted  from input box
                if event.key == K_BACKSPACE and len(mass_val) > 0:
                    mass_val = mass_val[:-1]
                elif event.key == pygame.K_RETURN and len(mass_val) > 0:
                    mass_active = False
                elif event.key != K_BACKSPACE: # If keyboard event not backspace is pressed .....
                    mass_val += event.unicode  # ... Add the text input

            if MASS_inp_rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                mass_active = False
                MASS_active = True
                velocity_active = False
            if event.type == pygame.KEYDOWN and MASS_active:
                if event.key == K_BACKSPACE and len(MASS_val) > 0:
                    MASS_val = MASS_val[:-1]
                elif event.key == pygame.K_RETURN and len(MASS_val) > 0:
                    MASS_active = False
                elif event.key != K_BACKSPACE:
                    MASS_val += event.unicode

            if velocity_inp_rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                mass_active = False
                MASS_active = False
                velocity_active = True
            if event.type == pygame.KEYDOWN and velocity_active:
                if event.key == K_BACKSPACE and len(velocity_val) > 0:
                    velocity_val = velocity_val[:-1]
                elif event.key == pygame.K_RETURN and len(velocity_val) > 0:
                    velocity_active = False
                elif event.key != K_BACKSPACE:
                    velocity_val += event.unicode

        if state == "start": # If the simulation has started and.......
            if pause_rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN : # User clicked on pause button............
                state = "setup orbit"     #return to orbit setup state
                

    time = (pygame.time.get_ticks()) / 1000 # divide time from time.get_ticks since start of program by 1000 to give time in seconds and not miliseconds
    screen.blit(black, (0, 0)) # print black background here
    T = smallfont.render(f"Time = {time}", True, 'White')
    T_rect = T.get_rect(center=(600, 650)) # Print time calculated here

    if state == "home": 
        show_homescreen()   #Display homescreen
        screen.blit(T, T_rect)  #Display Time

    elif state == "setup orbit" :
        screen.blit(black, (0, 0))
        Show_Orbit()    #Display setup orbit
        index, inp_list, surf_list = text_output(mass_val, MASS_val, velocity_val)

        if exit_rect.collidepoint(pos) and pygame.mouse.get_pressed():      #If exit button pressed....
            state = "home"            
        if start_rect.collidepoint(pos):        #If start button pressed
            if pygame.mouse.get_pressed():
                #last_time = ((pygame.time.get_ticks()) / 1000)

                if "e" in velocity_val:
                    velocity_vals = velocity_val.split("e")
                    vel_base = velocity_vals[0]
                    vel_p_exp = velocity_vals[1]
                    
                else:
                    vel_base = velocity_val
                    vel_p_base = 10
                    vel_p_exp = 0

                if "e" in mass_val:
                    mass_vals = mass_val.split("e")
                    mass_base = mass_vals[0]
                    mass_p_exp = mass_vals[1]

                if "e" in MASS_val:
                    MASS_vals = MASS_val.split("e")
                    Mass = MASS_vals[0]
                    MASS_p_exp = MASS_vals[1]
               
                G = 6.674*(10**-11)
                vx = float(vel_base) * (float(vel_p_base) ** (float(vel_p_exp)))
                vy = 0.0
                v = vx
                MASS_pos = (350*pixel, 350*pixel)
                MASS_pos_ap = (350,350)
                mass_pos_ap = (350,516)
                mass_pos = (350*pixel, 516*pixel)
                m = float(mass_base) * (float(10) ** (float(mass_p_exp)))   #Mass of test body(body A)
                M = float(Mass) * (float(10) ** (float(MASS_p_exp)))    #Mass of central body (body B)
                dx = 0
                dy = (516-350)*pixel    #initial displacement
                state = "start"     

                Expected_E =  0.5*m*vx*vx +(-(G*M*m)/dy)    #Expected energy is the total initial energy of system
                Expected_E_Mantissa,Expected_E_exp = math.frexp(Expected_E)
                Expected_E_text = tinyfont.render("Expected Energy = ", True, "White")
                Expected_E_rect = Expected_E_text.get_rect(topleft=(500,100))
                innitialisation = False #  extr values need to be initialised, if they are not then do this
                Centre_Mass = CenterBody(M,pixel)   #Creating an object 
    elif state == "start" :

        black.fill('Black') #background is black
        screen.blit(black,(0,0))


        pygame.draw.circle(screen, "White", MASS_pos_ap,10.0)#cant use the actual mass position as it would exceed the 700x700 pixel window screen. Hence, it is converted to pixels and rounded off to be mapped onto the display window
        pygame.draw.circle(screen, "White", mass_pos_ap,5.0)#cant use the actual mass position as it would exceed the 700x700 pixel window screen. Hence, it is converted to pixels and rounded off to be mapped onto the display window

        pygame.draw.rect(screen, "#EC4848", pause_rect, 5)  #pause icon outline
        screen.blit(pause_text, pause_rect)
        pygame.draw.rect(screen, "#336363", info_rect, 5)   #Info rectangle outline
        screen.blit(info_text, info_rect)
        dt = 1250  #Large time step (in seconds) so that the orbit takes place quickly.  A time step is the amount of time that passes between each iteration. multiple iterations (about 60) take place each second, hence a lot of time passes eah second
        if integrator == "Velocity":
        
        
            if innitialisation == False: # If this is not done to initialise the values, the program will crash
                angle,d = get_d(mass_pos, Centre_Mass.pos)
                Force = get_Force(d,m,M)
                a = get_acc(Force,m,d,angle)
                ax = a * math.cos(angle)
                ay = a * math.sin(angle)
            Centre_Mass.updatepos(dt,innitialisation,m,Force,mass_pos) #Updates the position of the central body using a velocity verlet integrator and energy of the central body 
            innitialisation = True

            #Using a velocity verlet integrator the objects position is changed to reflect the theoretical change in position in time dt
            new_dx = (vx*dt) + 0.5*ax*dt*dt    
            new_dy = (vy*dt) + 0.5*ay*dt*dt
            
            mass_pos =(mass_pos[0] + new_dx ,mass_pos[1]) 
            mass_pos =(mass_pos[0]  ,mass_pos[1] + new_dy)

            
            angle,d = get_d(mass_pos, Centre_Mass.pos)
            new_Force = get_Force(d,m,M)
            new_a = -new_Force/m
            new_ax = new_a * math.cos(angle)
            new_ay = new_a * math.sin(angle)
            new_vx = vx + 0.5*(ax + new_ax) *dt #New values of vx and vy are obtained for the next iteration
            new_vy = vy + 0.5*(ay + new_ay) *dt
            vx,vy = new_vx,new_vy
            ax,ay = new_ax,new_ay

            
        elif integrator == "Euler":
            angle,d = get_d(mass_pos, Centre_Mass.pos)
            Force = get_Force(d,m,M)
            a = get_acc(Force,m,d,angle)#Getting acceleration after time dt
            ax = a * math.cos(angle) 
            ay = a * math.sin(angle)    #Getting vector components of acceleration
            vx = vx + ax*dt     #Getting vector components of velocity after time dt
            vy = vy + ay*dt
            dx = vx*dt     #Getting vector components of change in displacement after time dt
            dy = vy*dt
            
            mass_pos = [mass_pos[0] + dx,mass_pos[1]]       #changing position of test mass 
            mass_pos = [mass_pos[0] ,mass_pos[1] + dy]
            Centre_Mass.updatepos(dt,innitialisation,m,Force,mass_pos)

        v = ((vx*vx) + (vy*vy))**0.5

        Actual_E =  0.5*m*v*v + Centre_Mass.energy +(-(G*m*M)/d)        #Calculating total energy of system by adding energy of test body and of Central body
        Actual_E_Mantissa,Actual_E_exp = math.frexp(Actual_E) 
        if info_rect.collidepoint(pos) and pygame.mouse.get_pressed():# If the mouse hovers over the info button , the expected energy(starting energy of the system) and the actual energy is displayed along with the percentage error
            
            Expected_E2_text = tinyfont.render(f"{round(Expected_E_Mantissa,4)} * 10 ^ {Expected_E_exp}",True,"White")
            Expected_E2_rect = Expected_E2_text.get_rect(topleft = (500,150))
            Actual_E_text = tinyfont.render("Actual Energy = ", True, "White")
            Actual_E_rect = Actual_E_text.get_rect(topleft=(500,200))
            Actual_E2_text = tinyfont.render(f"{round(Actual_E_Mantissa,4)} * 10 ^ {Actual_E_exp}",True,"White")
            Actual_E2_rect = Actual_E2_text.get_rect(topleft=(500,250))
            Error = ((Expected_E - Actual_E)/(Expected_E) * 100)        # Percentage error being calculated
            Error_text = tinyfont.render("Percentage Error = ", True, "White")
            Error_rect = Error_text.get_rect(topleft=(500,300))
            Error_2_text = tinyfont.render(f" +- {abs(round(Error,4))}",True,"White")
            Error_2_rect = Error_2_text.get_rect(topleft=(500,350))

            screen.blit(Expected_E_text,Expected_E_rect)
            screen.blit(Expected_E2_text,Expected_E2_rect)      #Showing text for errors and energy calculated above
            screen.blit(Actual_E_text,Actual_E_rect)
            screen.blit(Actual_E2_text,Actual_E2_rect)
            screen.blit(Error_text,Error_rect)
            screen.blit(Error_2_text,Error_2_rect)
            

                

                

            
        

        
        mass_pos_ap = ( int(mass_pos[0]/pixel),int(mass_pos[1]/pixel)) # Mapping the theoretical position of the masses onto the 700x700 window
        MASS_pos_ap = ( int(Centre_Mass.pos[0]/pixel),int(Centre_Mass.pos[1]/pixel))
        pygame.draw.line(screen,"Yellow",MASS_pos_ap,mass_pos_ap,2) #Drawing a line between the Central body and test body

        if 15 >= int(d/pixel) :     #Function to check collision and send an appropriate output if it happens
            state = "collision"
    if state == "collision":
        Collision_popup()
        




    clock.tick(60) #Ensures 60 fps is max(hence 60 iterations per second of the main game loop)
    pygame.display.update() #The display screen needs to be updated so that all the changes to the screen are visible
