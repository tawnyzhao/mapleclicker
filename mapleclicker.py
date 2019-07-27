# 'The Hunt for Pianus'
# Clicker game to kill a big fish, collect gold and make friends with a monkey.
# Written by Tony Zhao, 2018-06-01

# Import modules
import random
try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# - - - IMAGE LOADING AND INITIALIZING GLOBAL CONSTANTS - - - #

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 800

# Y-value where all characters stand
GROUND_LEVEL = CANVAS_HEIGHT/2
# Default character and enemy positions
CHARACTER_POSITION = [60*CANVAS_WIDTH/100, GROUND_LEVEL]
ENEMY_POSITION = [85*CANVAS_WIDTH/100, GROUND_LEVEL]
# Coordinates for where to spawn damage numbers
CHARACTER_NUMBER_SPAWN = [60*CANVAS_WIDTH/100, GROUND_LEVEL - 70]
ENEMY_NUMBER_SPAWN = [85*CANVAS_WIDTH/100, GROUND_LEVEL - 70]

# URLS for images 
HUD_URLS = ["https://i.imgur.com/OKT3T8A.png", # Main Banner
            "https://i.imgur.com/tJMuM0p.png" # Button
           ]
ENEMY_URLS = ["https://i.imgur.com/7D67yCt.png", # Sailor
              "https://i.imgur.com/YkVScxA.png", # Snake
              "https://i.imgur.com/08tayyl.png", # Cubic Slime
              "https://i.imgur.com/9lh4LE6.png", # Flat Slime
              "https://i.imgur.com/qEunPHx.png", # Rat
              "https://i.imgur.com/f1bndy3.png", # Skeleboy
              "https://i.imgur.com/uD3Lr7L.png", # Zhu Bajie
              "https://i.imgur.com/6b6X3rX.png", # Jar of Greed
              "https://i.imgur.com/NgpE2kl.png", # Genie
              "https://i.imgur.com/J4ubXbS.png", # Sea Serpent
              "https://i.imgur.com/pRJ51zy.png", # Tribal Warrior
              "https://i.imgur.com/ULuifH7.png", # Freedom Eagle
              "https://i.imgur.com/kAgoQmy.png", # Josh's Baby
              "https://i.imgur.com/GZsGIgD.png", # Siren
              "https://i.imgur.com/HpgUyhr.png", # Terence's Dino-Cnidarian
              "https://i.imgur.com/DfHTlf6.png", # SUCCubus
              "https://i.imgur.com/j5WFI9F.png", # EggBoy
              "https://i.imgur.com/zlBJKb1.png", # Dark Unicorn
              "https://i.imgur.com/U2rlRq4.png", # Pixie
              "https://i.imgur.com/XRf0SLZ.png", # Minitaur
              "https://i.imgur.com/0a7DC44.png", # Stone Golem
              "https://i.imgur.com/fuM4tfj.png", # Red Drake
             ]
BG_URLS = ["https://2.bp.blogspot.com/-g2KPkzdjasI/UjrjV8842TI/AAAAAAAABXo/oNx1BHOIsBw/s1600/Outdoor+Anime+Landscape+%5BScenery+-+Background%5D+68.jpg", # Beach
          "https://www.ihdimages.com/wp-content/uploadsktz/2014/11/anime_scenery_wallpaper_free_hd.jpg" # Plains
          ]
ALLY_URLS = ["https://i.imgur.com/CRH3ZZN.gif", # Monkey
             "https://d1u5p3l4wpay3k.cloudfront.net/terraria_fr_gamepedia/0/09/Hollandais_volant.png", # Airship
             "https://i.imgur.com/v7MvbiU.png",# Sword Girl
             "https://i.imgur.com/sShISL5.png", # Sword Boy
             "https://i.imgur.com/6xyWRYG.png", # Water Girl
             "https://i.imgur.com/dsl0eM4.gif" # Black Boy
            ]
PLAYER_IMAGE = simplegui.load_image("https://i.imgur.com/48tkXPh.png")
CLICK_SPRITE = simplegui.load_image("https://i.imgur.com/J8svLxK.png")
DAMAGE_NUMBERS_SPRITE = simplegui.load_image("https://i.imgur.com/tcfaWOh.png")
WATER_PROJECTILE_IMG = simplegui.load_image("https://i.imgur.com/4uGIBdk.png")
BLACK_PROJECTILE_IMG = simplegui.load_image("https://orig00.deviantart.net/06e9/f/2013/226/d/d/antasmunchie_pixel_by_villainvoices-d6i55rg.png")
GOLD_BAG_IMG = simplegui.load_image("https://vignette.wikia.nocookie.net/battlenations/images/c/c4/Gold_purse.png")
SKULL_IMG = simplegui.load_image("https://www.spreadshirt.ie/image-server/v1/mp/designs/11510433,width=178,height=178/pixel-skull-totenkopf.png")
BOSS_IMG = simplegui.load_image("https://cdn.wikimg.net/en/strategywiki/images/9/90/MS_Monster_Pianus_%28Right_Side%29.png") # Pianus
# Load image urls into a list of objects
BG_IMGS = [simplegui.load_image(URL) for URL in BG_URLS]
ENEMY_IMGS = [simplegui.load_image(URL) for URL in ENEMY_URLS]
HUD_IMGS = [simplegui.load_image(URL) for URL in HUD_URLS]
ALLY_IMGS = [simplegui.load_image(URL) for URL in ALLY_URLS]
# Dictionary of all image dimensions
IMG_SIZES = {PLAYER_IMAGE: (88, 88),
            DAMAGE_NUMBERS_SPRITE: ((4, 7), (80/10, 14)),
            WATER_PROJECTILE_IMG: (128, 128),
            BLACK_PROJECTILE_IMG: (195, 195),
            GOLD_BAG_IMG: (200, 210),
            ALLY_IMGS[0]: (56, 64),
            ALLY_IMGS[1]: (590, 534),
            ALLY_IMGS[2]: (80, 72),
            ALLY_IMGS[3]: (64, 64),
            ALLY_IMGS[4]: (96, 104),
            ALLY_IMGS[5]: (64, 96),
            CLICK_SPRITE: ((96, 96), (960/5, 384/2)),
            BG_IMGS[0]: (1024, 576),
            BG_IMGS[1]: (1631, 1050),
            ENEMY_IMGS[0] : (56, 64),
            ENEMY_IMGS[1] : (64, 48),
            ENEMY_IMGS[2]: (32, 32),
            ENEMY_IMGS[3]: (32, 32),
            ENEMY_IMGS[4]: (48, 32),
            ENEMY_IMGS[5]: (64, 56),
            ENEMY_IMGS[6]: (96, 48),
            ENEMY_IMGS[7]: (88, 96),
            ENEMY_IMGS[8]: (56, 80),
            ENEMY_IMGS[9]: (72, 80),
            ENEMY_IMGS[10]: (88, 54),
            ENEMY_IMGS[11]: (64, 72),
            ENEMY_IMGS[12]: (48, 56),
            ENEMY_IMGS[13]: (72, 80),
            ENEMY_IMGS[14]: (47, 56),
            ENEMY_IMGS[15]: (88, 104),
            ENEMY_IMGS[16]: (56, 56),
            ENEMY_IMGS[17]: (64, 64),
            ENEMY_IMGS[18]: (40, 56),
            ENEMY_IMGS[19]: (120, 96),
            ENEMY_IMGS[20]: (128, 104),
            ENEMY_IMGS[21]: (88, 120),
            BOSS_IMG: (416, 364),
            HUD_IMGS[0]: (509, 336),
            HUD_IMGS[1]: (104, 102),
            SKULL_IMG: (178, 178)
            }

# Enemy stats
ENEMY_LIST = [('Sailor', ENEMY_IMGS[0], 5, 2, 1),
             ('Snake', ENEMY_IMGS[1], 10, 2, 1),
             ('Cubic Slime', ENEMY_IMGS[2], 20, 5, 5),
             ('Elliptical Slime', ENEMY_IMGS[3], 50, 5, 7),
             ('Rat', ENEMY_IMGS[4], 100, 5, 5),
             ('SkeleBoy', ENEMY_IMGS[5], 500, 8, 20),
             ('Zhu Bajie', ENEMY_IMGS[6], 1500, 10, 30),
             ('Jar of Greed', ENEMY_IMGS[7], 3000, 5, 100),
             ('Genie', ENEMY_IMGS[8], 5000, 13, 300),
             ('Sea Serpent', ENEMY_IMGS[9], 10000, 15, 500),
             ('Tribal Warrior', ENEMY_IMGS[10], 20000, 20, 1000),
             ('Freedom Eagle', ENEMY_IMGS[11], 35000, 22, 2000),
             ("Baby", ENEMY_IMGS[12], 50000, 26, 4000),
             ('Siren', ENEMY_IMGS[13], 75000, 30, 3600),
             ("Dino-Cnidarian", ENEMY_IMGS[14], 100000, 35, 10000),
             ('SUCCubus', ENEMY_IMGS[15], 150000, 40, 20000),
             ('EggBoy', ENEMY_IMGS[16], 200000, 50, 10000),
             ('Black Unicorn', ENEMY_IMGS[17], 400000, 75, 50000),
             ('Pixie', ENEMY_IMGS[18], 700000, 85, 100000),
             ('Minitaur', ENEMY_IMGS[19], 1000000, 100, 500000),
             ('Stone Golem', ENEMY_IMGS[20],1400000, 120, 1000000),
             ('Red Drake', ENEMY_IMGS[21],2000000, 180, 2000000),
             ]
# Stats for final boss
PIANUS_STATS = ('Pianus', BOSS_IMG, 100000000, 300, 10000000, True)
# Unlockable allies
LOCKED_ALLIES = [("Sword Boy", ALLY_IMGS[3], [50*CANVAS_WIDTH/100, GROUND_LEVEL+5], 1.3, 50, 100),
                 ("Sword Girl", ALLY_IMGS[2], [40*CANVAS_WIDTH/100, GROUND_LEVEL-1], 1.5, 300, 100),
                 ("Monkey", ALLY_IMGS[0], [30*CANVAS_WIDTH/100, GROUND_LEVEL+7], 1.3, 1000, 100),
                 ("Black Boy", ALLY_IMGS[5], [20*CANVAS_WIDTH/100, GROUND_LEVEL-17], 3, 8000, 100),
                 ("Water Girl", ALLY_IMGS[4], [8*CANVAS_WIDTH/100, GROUND_LEVEL - 22], 1.7, 10000, 150),
                 ("Airship", ALLY_IMGS[1], [10*CANVAS_WIDTH/100, GROUND_LEVEL-555], 2, 50000, 700)]       


# - - - GLOBAL VARIABLES - - - #

# List of HUD and NPC objects
buttons = []
hitmarkers = []
allies = []
projectiles = [] 
damage_numbers = []
current_bg = BG_IMGS[0]
# Boolean for whether character has died. Starts game at True. 
blacked_out = True
gold = 0
level = 1
bosses_killed = 0 
# Upgrade costs
upgrade_cost = 10
# List of costs for recruiting an ally, set False once all allies have been recruited
r_cost_list = [50, 750, 5000, 10000, 200000, 1000000, False]
r_index = 0 # Current cost from cost list
recruit_cost = r_cost_list[r_index]
heal_cost = 60


# Helper function to find distance between two points, using the Pythogorean Theorem
def get_dist(pos1, pos2):
    return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5


# Helper function to simulate level-ups for allies
def init_stat(level, growth):
    result = 0
    for i in range(level):
        result += (i)**growth * i * 0.5
    return result    



# ----- CLASSES ----- #



class Character:
    def __init__(self, health, attack):
        self.health = health
        self.max_health = health
        self.attack = attack
        self.image = PLAYER_IMAGE
        self.pos = [CHARACTER_POSITION[0], CHARACTER_POSITION[1]]
        self.vel = [0,0]
        self.length = 100
        self.rotation  = 0 
        self.time = 0.0
        
    def draw(self, canvas):
        canvas.draw_image(self.image, 
                         (IMG_SIZES[self.image][0]/2, IMG_SIZES[self.image][1]/2),
                         IMG_SIZES[self.image],
                         self.pos,
                         (self.length, self.length),
                         self.rotation)
        
    def update(self):
        self.pos[0] += self.vel[0]
        # Makes character step after an attack
        if self.pos[0] >= CHARACTER_POSITION[0] + 25:
            self.vel[0] = -5
        elif self.pos[0] < CHARACTER_POSITION[0]:
            self.vel = [0, 0]
            self.pos[0] = CHARACTER_POSITION[0]
            
    def auto_attack(self):
        global current_enemy
        if not blacked_out:
            self.time += 1
            # Automatic attacking
            if self.time >= 60:
                damage = int(self.attack * random.randrange(90,110)*0.01) + 1
                current_enemy.health -= damage
                hitmarkers.append(Hitmarker(ENEMY_POSITION))
                generate_damage_numbers(damage, [ENEMY_NUMBER_SPAWN[0],ENEMY_NUMBER_SPAWN[1]])
                self.vel = [10,0]
                self.time = 0
                
    def level_up(self):
        # Increases stats
        self.attack += (level)**3
        self.max_health += (level)**2
        self.health = self.max_health
       
    
class Enemy:
    def __init__(self, name, image, health, attack, gold, boss = False):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack
        self.gold = gold
        self.is_boss = boss
        self.image = image
        self.vel = [0,0]
        self.rotation = 0
        # Sets dimensions based on enemy type
        if self.is_boss:
            self.length = 500
            self.pos = [ENEMY_POSITION[0] + 75, ENEMY_POSITION[1]-75]
            self.orig_pos = (self.pos[0], self.pos[1])
        else:
            self.length = 100
            self.pos = [ENEMY_POSITION[0], ENEMY_POSITION[1]]
            self.orig_pos = (self.pos[0], self.pos[1])
        self.time = 20
        self.is_animated = False
        
    def draw(self, canvas):
        canvas.draw_image(self.image,
                         (IMG_SIZES[self.image][0]/2, IMG_SIZES[self.image][1]/2),
                         IMG_SIZES[self.image],
                         self.pos,
                         [self.length, self.length],
                         self.rotation)
        
    def update(self):
        self.pos[0] += self.vel[0]
        # Makes enemy step after an attack
        if self.pos[0] <= self.orig_pos[0] - 25:
            self.vel[0] = 5
        elif self.pos[0] > self.orig_pos[0]:
            self.vel = [0, 0]
            self.pos[0] = self.orig_pos[0]
            self.is_animated = False
            
    def has_hit(self, position):
        # Extra +40 in collision for ease of clicking on enemy
        if get_dist(position, self.pos) < self.length/2 + 40:
            return True
        
    def give_gold(self):
        global gold, bosses_killed, upgrade_cost
        # Reward for killing Pianus
        if self.is_boss:
            upgrade_cost = 10
            bosses_killed += 1
        gold += self.gold
        
    def auto_attack(self):
        self.time += 1
        if not blacked_out:
            if self.time > 60:
                damage = int(self.attack * random.randrange(90,110)*0.01) + 1
                character.health -= damage
                hitmarkers.append(Hitmarker(CHARACTER_POSITION))
                generate_damage_numbers(damage, [CHARACTER_NUMBER_SPAWN[0], CHARACTER_NUMBER_SPAWN[1]])
                self.vel = [-10,0]
                self.is_animated = True
                self.time = 0                    

                
class Button:
    def __init__(self, image, function, position, dimensions):
        self.image = image
        self.function = function
        self.pos = position
        self.dim = dimensions
        self.color = "Black"
        
    def draw(self, canvas):
        global blacked_out
        # Basic Button Draws
        canvas.draw_image(self.image,
                         (IMG_SIZES[self.image][0]/2, IMG_SIZES[self.image][1]/2),
                         IMG_SIZES[self.image],
                         self.pos,
                         self.dim)
        canvas.draw_text(self.function, (self.pos[0] - 0.5*frame.get_canvas_textwidth(self.function, 20, 'sans-serif')-1, self.pos[1]), 20, self.color) # Offset by -1 to account for disjointed button image
        # Unique Button Draws
        if self.function == "Continue":
            canvas.draw_text("Press Continue to start the game.", (240,555), 14, 'Red')
            canvas.draw_text("Click the enemy to attack! If you die, you lose all your gold. Killing an enemy restores some health.", (240,575), 14, 'Black')
            canvas.draw_text("'Recruit' to hire an ally to help you fight. 'Level-Up!' to increase your damage and unlock enemies.", (240,595), 14, 'Black')
            canvas.draw_text("'Heal' to restore your health to full.", (240,615), 14, 'Black')
            canvas.draw_text("Good luck killing the legendary fish Pianus!", (240,635), 14, 'Black')
        elif self.function == "Revive" and blacked_out:
            canvas.draw_text("All Gold", (775, 705), 20, 'Black')
            canvas.draw_image(GOLD_BAG_IMG,
                            (IMG_SIZES[GOLD_BAG_IMG][0]/2,IMG_SIZES[GOLD_BAG_IMG][1]/2),
                            IMG_SIZES[GOLD_BAG_IMG],
                            (750, 705),
                            (50, 50))
        elif self.function == "Recruit" and not blacked_out:
            canvas.draw_text(str(recruit_cost) + " Gold", (175, 705), 20, 'Black')
            canvas.draw_image(GOLD_BAG_IMG,
                         (IMG_SIZES[GOLD_BAG_IMG][0]/2,IMG_SIZES[GOLD_BAG_IMG][1]/2),
                         IMG_SIZES[GOLD_BAG_IMG],
                         (150, 705),
                         (50, 50))
        elif self.function == "Level-Up!" and not blacked_out:
            canvas.draw_text(str(upgrade_cost) + " Gold", (375, 705), 20, 'Black')   
            canvas.draw_image(GOLD_BAG_IMG,
                         (IMG_SIZES[GOLD_BAG_IMG][0]/2,IMG_SIZES[GOLD_BAG_IMG][1]/2),
                         IMG_SIZES[GOLD_BAG_IMG],
                         (350, 705),
                         (50, 50))
        elif self.function == "Heal" and not blacked_out:
            canvas.draw_text(str(heal_cost) + " Gold", (575, 705), 20, 'Black')
            canvas.draw_image(GOLD_BAG_IMG,
                         (IMG_SIZES[GOLD_BAG_IMG][0]/2,IMG_SIZES[GOLD_BAG_IMG][1]/2),
                         IMG_SIZES[GOLD_BAG_IMG],
                         (550, 705),
                         (50, 50))
        elif self.function == "Fight Pianus":
            canvas.draw_text("WARNING:", (340, 620), 20, 'Black')
            canvas.draw_text("Pianus is powerful", (340, 645), 20, 'Black')
            canvas.draw_text("But he tastes great!", (340, 670), 20, 'Black')
            canvas.draw_image(SKULL_IMG,
                         (IMG_SIZES[SKULL_IMG][0]/2,IMG_SIZES[SKULL_IMG][1]/2),
                         IMG_SIZES[SKULL_IMG],
                         (310,645),
                         (50,50))
    def activate(self):
        # Behaviour on click 
        global LOCKED_ALLIES, allies, recruit_cost, r_index, r_cost_list, gold, upgrade_cost, heal_cost, blacked_out, current_enemy
        if self.function == "Recruit" and not blacked_out:
            if len(LOCKED_ALLIES) > 0 and gold >= recruit_cost:
                gold -= recruit_cost
                allies.append(Ally(*LOCKED_ALLIES[0]))
                # Removes ally from locked allies list
                LOCKED_ALLIES = LOCKED_ALLIES[1:]
                r_index += 1
                recruit_cost = r_cost_list[r_index]
                if len(LOCKED_ALLIES) == 0:
                    self.function = "All Unlocked!"
        elif self.function == "Level-Up!" and gold >= upgrade_cost and not blacked_out:
            global level, current_enemy
            level += 1
            character.level_up()
            for ally in allies:
                ally.level_up()
            gold -= upgrade_cost
            upgrade_cost *= 2.5
            upgrade_cost = int(upgrade_cost)
        elif self.function == "Heal" and gold >= heal_cost and not blacked_out:
            character.health = character.max_health
            gold -= heal_cost
            heal_cost = character.max_health * 2
        elif self.function == "Revive" and blacked_out:
            gold = 0
            character.health = character.max_health
            if level < len(ENEMY_LIST):    
                new_enemy = ENEMY_LIST[random.randrange(0,level + 1)]
                # the * converts a list into arguments
                current_enemy = Enemy(*new_enemy)
            else:
                # case to avoid index being out of range of list
                current_enemy = Enemy(*random.choice(ENEMY_LIST))
            blacked_out = False
        elif self.function == "Continue":
            buttons.append(Button(HUD_IMGS[0], "Revive", (800,750), (200,100)))
            blacked_out = False
            self.function = "Fight Pianus"
        elif self.function == "Fight Pianus" and not blacked_out:
            # spawns boss
            current_enemy = Enemy(*PIANUS_STATS)
            
    def update(self):
        # Changes color of the text on the button to red if it is unusable
        global gold, recruit_cost, upgrade_cost, heal_cost
        if self.function == "Recruit":
            if gold < recruit_cost or blacked_out:
                self.color = "Red"
            else:
                self.color = "Black"
        elif self.function == "Level-Up!":
            if gold < upgrade_cost or blacked_out:
                self.color = "Red"
            else:
                self.color = "Black"
        elif self.function == "Heal":
            if gold < heal_cost or blacked_out:
                self.color = "Red"
            else:
                self.color = "Black"
        elif self.function == "Revive":
            if blacked_out:
                self.color = "Black"
            else:
                self.color = "Red"
        elif self.function == "Fight Pianus":
            if blacked_out:
                self.color = "Red"
            else:
                self.color = "Black"
                
    def has_hit(self, position):
        # Function to find collision of a square object
        within_x = False
        within_y = False
        x_range = (self.pos[0] - self.dim[0]/2, self.pos[0] + self.dim[0]/2)
        y_range = (self.pos[1] - self.dim[1]/2, self.pos[1] + self.dim[1]/2)
        if position[0] < x_range[1] and position[0] > x_range[0]:
            within_x = True
        if position[1] < y_range[1] and position[1] > y_range[0]:
            within_y = True
        if within_x and within_y:
            return True


class Hitmarker:
    def __init__(self, position):
        self.time = 0
        self.image = CLICK_SPRITE
        self.pos = position
        self.length = 100
        
    def draw(self,canvas):
        # Sprite animation
        tile_center = [IMG_SIZES[self.image][0][0] + int(self.time)%5 * IMG_SIZES[self.image][1][0],
                      IMG_SIZES[self.image][0][1] + int(self.time)//5 * IMG_SIZES[self.image][1][1]]
        canvas.draw_image(self.image, 
                         tile_center, 
                         IMG_SIZES[self.image][1], 
                         self.pos, 
                         [self.length,self.length])
        
    def update(self):
        self.time += 0.5

        
class Ally:
    def __init__(self, name, image, position, growth, attack, length):
        global level
        self.name = name
        self.image = image
        self.pos = position
        self.original_pos = [self.pos[0], self.pos[1]]
        self.growth = growth # How much stats increase on a level up
        self.attack = attack + init_stat(level, growth)
        self.time = 0
        self.vel = [0, 0]
        self.length = [IMG_SIZES[image][0]*1.5, IMG_SIZES[image][1]*1.5]
        
    def draw(self, canvas):
        canvas.draw_image(self.image, 
                         (IMG_SIZES[self.image][0]/2, IMG_SIZES[self.image][1]/2),
                         IMG_SIZES[self.image],
                         self.pos,
                         self.length)
        
    def update(self):
        self.pos[0] += self.vel[0]
        # Makes step after animation
        if self.pos[0] >= self.original_pos[0] + 25:
            self.vel[0] = -5
        elif self.pos[0] < self.original_pos[0]:
            self.vel = [0, 0]
            self.pos[0] = self.original_pos[0]
            
    def level_up(self):
        self.attack += 0.5 * level* level**(self.growth)
        
    def auto_attack(self, canvas):
        global current_enemy, bosses_killed
        damage = int(self.attack * random.randrange(90,110)*0.01) + 1
        if not blacked_out:
            if self.name == "Airship":
                self.time += 1
                if self.time >= 180:
                    if self.time % 5 == 0:
                        current_enemy.health -= damage
                        hitmarkers.append(Hitmarker(ENEMY_POSITION))
                        generate_damage_numbers(damage, [ENEMY_NUMBER_SPAWN[0],ENEMY_NUMBER_SPAWN[1]])
                        canvas.draw_line((255, 132), ENEMY_POSITION, 16, 'Red')
                    if self.time >= (300 * (bosses_killed + 1)):
                        canvas.draw_line((255, 132), ENEMY_POSITION, 16, 'Red')
                        self.time = 0    
            elif self.name == "Black Boy":
                self.time += 1 * (bosses_killed + 1)
                if self.time >= 60:
                    projectiles.append(Projectile(BLACK_PROJECTILE_IMG, [190,330],[12,1.5],damage,70))
                    self.time = 0
            elif self.name == "Water Girl":
                self.time += 1 * (bosses_killed + 1)
                if self.time >= 10:
                    projectiles.append(Projectile(WATER_PROJECTILE_IMG, [100,320],[24,3],damage,50))
                    self.time = 0
            elif self.name == "Monkey":
                self.time += 1
                if self.time >= 10:
                    current_enemy.health -= damage
                    hitmarkers.append(Hitmarker(ENEMY_POSITION))
                    generate_damage_numbers(damage, [ENEMY_NUMBER_SPAWN[0], ENEMY_NUMBER_SPAWN[1]])
                    self.vel = [10,0]
                    self.time = 0
            else:
                self.time += 1
                if self.time >= 30:
                    current_enemy.health -= damage
                    hitmarkers.append(Hitmarker(ENEMY_POSITION))
                    generate_damage_numbers(damage, [ENEMY_NUMBER_SPAWN[0], ENEMY_NUMBER_SPAWN[1]])
                    self.vel = [10,0]
                    self.time = 0

                    
class Damage_Number:
    def __init__(self, value, position):
        self.value = str(value)
        self.pos = position
        self.vel = [0,-4]
        
    def draw(self, canvas):
        # draws numbers based on values mapped to a spritesheet and adjusts so they are centered
        for i in range(len(self.value)):
            canvas.draw_image(DAMAGE_NUMBERS_SPRITE,
                              [IMG_SIZES[DAMAGE_NUMBERS_SPRITE][0][0] + (int(self.value[i])) * 8,
                               IMG_SIZES[DAMAGE_NUMBERS_SPRITE][0][1]],
                               IMG_SIZES[DAMAGE_NUMBERS_SPRITE][1],
                               [self.pos[0] - len(self.value)*10 + i*20, self.pos[1]],
                               (20,50))
            
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
    def is_offscreen(self): # To check if numbers are off-screen for removal
        if self.pos[1] < -50: 
            return True
        
        
class Projectile:
    def __init__(self, image, position, velocity, attack, length):
        self.image = image
        self.pos = position
        self.vel = velocity
        self.attack = attack
        self.length = length
        
    def draw(self, canvas):
        canvas.draw_image(self.image,
                         (IMG_SIZES[self.image][0]/2, IMG_SIZES[self.image][1]/2),
                         IMG_SIZES[self.image],
                         self.pos,
                         (self.length,self.length))
        
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
    def has_hit(self):
        # Seperate to adjust for Pianus' sprite being disjointed
        if current_enemy.is_boss:
            if get_dist(self.pos, ENEMY_POSITION) <= current_enemy.length/2 - 100:
                return True
        else:            
            if get_dist(self.pos, ENEMY_POSITION) <= current_enemy.length/2:
                return True


# - - - KEY HANDLERS - - - #
def keydown(key):
    pass
def keyup(key):
    pass
def mouse_click(position):
    if not blacked_out:
        # Attack click
        if current_enemy.has_hit(position):
            damage = int(character.attack * random.randrange(90,110)*0.01) + 1
            current_enemy.health -= damage
            hitmarkers.append(Hitmarker(position))
            generate_damage_numbers(damage, [ENEMY_NUMBER_SPAWN[0], ENEMY_NUMBER_SPAWN[1]])
            character.vel = [10,0]    
    for button in buttons:
        # Button use
        if button.has_hit(position):
            button.activate()
            hitmarkers.append(Hitmarker(position))
            
# Initializes objects from classes
character = Character(30,1)
current_enemy = Enemy(*ENEMY_LIST[0])
buttons.append(Button(HUD_IMGS[0], "Level-Up!", (400,750), (200,100)))
buttons.append(Button(HUD_IMGS[0], "Recruit", (200,750), (200,100)))
buttons.append(Button(HUD_IMGS[0], "Heal", (600,750), (200,100)))
buttons.append(Button(HUD_IMGS[0], "Continue", (600,650), (200,100)))

# Checks to see if enemy is dead, and generates new enemy
def generate_enemy():
    global current_enemy
    if current_enemy.health <= 0 and current_enemy.is_animated == False:
        # Randomly chooses a new enemy from the list
        current_enemy.give_gold()
        if character.health + current_enemy.attack <= character.max_health:
            character.health += current_enemy.attack
        else:
            character.health = character.max_health
        if level < len(ENEMY_LIST):    
            new_enemy = ENEMY_LIST[random.randrange(0,level + 1)]
            # the * converts a list into arguments
            current_enemy = Enemy(*new_enemy)
        else:
            # case to avoid index being out of range of list
            current_enemy = Enemy(*random.choice(ENEMY_LIST))

# Function to generate damage numbers
def generate_damage_numbers(attack, position):
    damage_numbers.append(Damage_Number(attack, position))


# - - - DRAW HANDLER AND INITIALIZING FRAMES - - - #
def draw(canvas):
    global blacked_out
    generate_enemy()
    
    # Background Image
    canvas.draw_image(current_bg,
                      (IMG_SIZES[current_bg][0]/2,IMG_SIZES[current_bg][1]/2),
                      IMG_SIZES[current_bg],
                      (CANVAS_WIDTH/2, CANVAS_HEIGHT/3),
                      (CANVAS_WIDTH, 2*CANVAS_HEIGHT/3))
    
    current_enemy.draw(canvas)
    current_enemy.auto_attack()
    current_enemy.update()
    for projectile in projectiles:
        projectile.draw(canvas)
        projectile.update()
        if projectile.has_hit():
            hitmarkers.append(Hitmarker(projectile.pos))
            generate_damage_numbers(projectile.attack, [ENEMY_NUMBER_SPAWN[0],ENEMY_NUMBER_SPAWN[1]])
            current_enemy.health -= projectile.attack
            projectiles.remove(projectile)
    for ally in allies:
        ally.draw(canvas)
        ally.auto_attack(canvas)
        ally.update()
    character.draw(canvas)
    character.auto_attack()
    character.update()
    
    # Checks if character has died
    if character.health <= 0:
        blacked_out = True
        character.health = 0
    # Draws floating damage numbers
    for damage_number in damage_numbers:
        damage_number.draw(canvas)
        damage_number.update()
        # Removes damage numbers after they leave the top of the screen
        if damage_number.is_offscreen():
            damage_numbers.remove(damage_number)
        
    # Menu background
    canvas.draw_image(HUD_IMGS[0],
                     (IMG_SIZES[HUD_IMGS[0]][0]/2,IMG_SIZES[HUD_IMGS[0]][1]/2),
                     IMG_SIZES[HUD_IMGS[0]],
                     (CANVAS_WIDTH/2+10, 9*CANVAS_HEIGHT/10),
                     (CANVAS_WIDTH+150, 4*CANVAS_HEIGHT/5))
    
    for button in buttons:
        button.draw(canvas)
        button.update()
    # Displays stats    
    canvas.draw_text("Gold: " + str(gold), (110,625), 20, 'Gold')
    canvas.draw_text("Level: " + str(level), (110,600), 20, 'Navy')
    canvas.draw_text("Health: " + str(character.health) + "/" + str(character.max_health), (110,575), 20, 'Red')
    canvas.draw_text("Attack: " + str(character.attack), (110,650), 20, 'Red')
    canvas.draw_text(str(current_enemy.name),(875 - frame.get_canvas_textwidth(str(current_enemy.name), 20, 'sans-serif'),575), 20, 'Black')
    canvas.draw_text(str(current_enemy.health)  + "/" + str(current_enemy.max_health), (875 - frame.get_canvas_textwidth(str(current_enemy.health)  + "/" + str(current_enemy.max_health), 20, 'sans-serif') ,600), 20, 'Navy')        
        
    for hitmarker in hitmarkers:
        hitmarker.draw(canvas)
        hitmarker.update()
        if hitmarker.time > 15:
            hitmarkers.remove(hitmarker)


frame = simplegui.create_frame("The Hunt for the Pianus", CANVAS_WIDTH, CANVAS_HEIGHT, 0)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(mouse_click)
frame.set_draw_handler(draw)
frame.start()
