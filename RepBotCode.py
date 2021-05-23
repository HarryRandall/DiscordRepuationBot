# Imports
#------------------------------------------------------------------------------------------------------------------------------
import discord
import discord.ext
from discord.ext.commands import Bot
from discord.ext import commands
import json
#------------------------------------------------------------------------------------------------------------------------------
# Globals
user_exists_in_json = False
#------------------------------------------------------------------------------------------------------------------------------
TOKEN = 'Private' #Bot Token (Secret)
bot = Bot(command_prefix='+') #Prefix for the bot
bot.remove_command('help') #Remove the original +rep command so I can make my own
#------------------------------------------------------------------------------------------------------------------------------
# Bot Turning On
@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
#------------------------------------------------------------------------------------------------------------------------------
# Json
#------------------------------------------------------------------------------------------------------------------------------
def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)
Json_Items = getJSON("./all_user_rep.json") #Open the JSON and store everything.
#------------------------------------------------------------------------------------------------------------------------------
# +help command
#------------------------------------------------------------------------------------------------------------------------------
@bot.command()
async def help(ctx):
    channel = bot.get_channel(845567167251742740)
    if ctx.channel.id == channel.id:
        embed=discord.Embed(title=f"Help", description=f"{ctx.author} please follow the syntax provided", color=0xf39c12)
        embed.add_field(name="syntax", value="+rep @user (Amount) (Gayzo, Imgur or Discord image)", inline=False)
        embed.add_field(name="Example", value=f"+rep {ctx.author} $25 https://gyazo.com/example", inline=False)
        embed.set_footer(text="Any issues dm Beetlemadooda#0955")
        await ctx.send(embed=embed, delete_after=10.0)
        await ctx.message.delete()
    else:
        return
#------------------------------------------------------------------------------------------------------------------------------
# +check @user command
#------------------------------------------------------------------------------------------------------------------------------
user_has_rep = False
@bot.command()
async def check(ctx, member:discord.User):
    global user_has_rep
    user_has_rep = False
    for i in range(0,len(Json_Items)): #It doesn't exist
        for x in Json_Items[i]:
            if int(x) == int(member.id):
                total_money = Json_Items[i][x]['Total_Deals_Amount']
                total_deals = Json_Items[i][x]['Total_Deals_Completed'] 
                embed=discord.Embed(title=f"Check", description=f"This is {member} rep!", color=0xe74c3c)
                embed.add_field(name="Total Deals", value=f"{member.mention} has completed a total of {total_deals} rep!", inline=False)
                embed.add_field(name="Total Amount", value=f"{member.mention} has an amount of ${total_money}!", inline=False)
                embed.set_footer(text="Any issues dm Beetlemadooda#0955")
                await ctx.send(embed=embed, delete_after=20.0)
                await ctx.message.delete()
                user_has_rep = True
    if user_has_rep == False:
        total_money = Json_Items[i][x]['Total_Deals_Amount']
        total_deals = Json_Items[i][x]['Total_Deals_Completed'] 
        embed=discord.Embed(title=f"Check", description=f"This is {member} rep!", color=0xe74c3c)
        embed.add_field(name="Total Deals", value=f"{member.mention} has 0 rep!", inline=False)
        embed.add_field(name="Total Amount", value=f"{member.mention} has an amount of $0!", inline=False)
        embed.set_footer(text="Any issues dm Beetlemadooda#0955")
        await ctx.send(embed=embed, delete_after=20.0)
        await ctx.message.delete()
        
#------------------------------------------------------------------------------------------------------------------------------
# +rep @user command
#------------------------------------------------------------------------------------------------------------------------------
@bot.command()
async def rep(ctx, member:discord.User, *args):
    global user_exists_in_json
    user_exists_in_json = False
    # Variables:
    all_currency_symbols = ['€', '£', '$', '¢', '_', '+', '=', ' ']

    #Code
    #Checks if all of the input fields are right
    channel = bot.get_channel(845567167251742740)
   
    if (len(args) < 1 or len(args) > 2 or member == ctx.author or member.id == 811474768636936212): 
        embed=discord.Embed(title=f"Error", description=f"{ctx.author} You have used the rep command incorrectly! Please follow the syntax below. (Make sure you are not repping yourself...)", color=0xf1c40f)
        embed.add_field(name="syntax", value="+rep @user (Amount) (Imgur, Gayzo or Discord Attachement)", inline=False)
        embed.add_field(name="Example", value=f"+rep {ctx.author} $25 https://gyazo.com/example", inline=False)
        embed.set_footer(text="Any issues dm Beetlemadooda#0955")
        await ctx.send(embed=embed, delete_after=10.0)
        await ctx.message.delete()
    else:
        if ctx.channel.id == channel.id:
            

        # Checks the money input
            if args[0][0] in all_currency_symbols: #If the amount is entered in as $5 it will remove it.
                money_input = args[0]
                money_input = args[0][1:]
            else:
                money_input = args[0]
        # Checks to see if the input is numerical
            if money_input.isdigit() == False or money_input == "0": 
                embed=discord.Embed(title=f"Error", description=f"{ctx.author} make sure that you have inputed an actual amount E.G $5 and it doesn't have a decimal!", color=0xf1c40f)
                embed.add_field(name="Rounding", value="Please Round the Amount to the Nearest Dollar!", inline=False)
                embed.add_field(name="Syntax", value="+rep @user (Amount) (Imgur, Gayzo or Discord Image)", inline=False)
                embed.add_field(name="Example", value=f"+rep {ctx.author} $25 https://gyazo.com/example", inline=False)
                embed.set_footer(text="Any issues dm Beetlemadooda#0955")
                await ctx.send(embed=embed, delete_after=10.0)
                await ctx.message.delete()
        # Flags for amounts of money
            else:
                if int(money_input) > 1000:
                    # await ctx.send("You have been given bannedfromtrading for fake repping. Dm Beetlemadooda#0955 or msg the support bot if this is a mistake.")
                    embed=discord.Embed(title=f"BannedFromTrading", description=f"{ctx.author.mention} You have been given bannedfromtrading for fake repping.\n\nDm Beetlemadooda#0955 or msg the support bot if this is a mistake.", color=0xf1c40f)
                    embed.set_thumbnail(url="https://www.telegraph.co.uk/content/dam/films/spark/warnerhomevideo/pennywise-xlarge.jpg?imwidth=1200")
                    embed.set_footer(text="Any issues dm Beetlemadooda#0955")
                    await ctx.author.send(embed=embed, delete_after=100.0)
                    await ctx.message.delete()
                    
        #This is the rep arguements:        
                else: 
        #Add and update the JSON
                    if int(money_input) > 500:
                        await ctx.send("@staffping please check if this is correct!")
                    if len(args) == 2: #Checks if there is a link (Gayzo or imgur)
                        if not (args[1].startswith("https://gyazo.com/") or args[1].startswith("https://i.imgur.com/")):
                            embed=discord.Embed(title=f"Error", description=f"{ctx.author.mention} You must include either a Gayzo, Imgur or Discord Image!", color=0xf1c40f)
                            embed.set_thumbnail(url="https://i.pinimg.com/originals/84/c0/1a/84c01aa60d96039f4aae384f59e0b6db.jpg")
                            embed.add_field(name="Syntax", value="+rep @user (Amount) (Gayzo, Imgur or discord image)", inline=False)
                            embed.add_field(name="Example", value=f"+rep {ctx.author} $25 https://gyazo.com/example", inline=False)
                            embed.add_field(name="Rounding", value="Please Round the Amount to the Nearest Dollar!", inline=False)
                            embed.set_footer(text="Any issues dm Beetlemadooda#0955")
                            await ctx.send(embed=embed, delete_after=10.0)
                            await ctx.message.delete()

                        else:
                            embed=discord.Embed(title=f"+Rep", description=f"{member} has been Repped!", color=0x00ffcc)
                            embed.set_thumbnail(url=f"{args[1]}")
                            embed.add_field(name="Amount", value=f"${money_input}", inline=False)
                            embed.add_field(name="Proof", value=f"{args[1]}", inline=False)
                            embed.add_field(name="User ID", value=f"Received: {member}, {member.id}\n Sent: {ctx.author}, {ctx.author.id}", inline=False)
                            embed.set_footer(text="Any issues dm Beetlemadooda#0955")
                            await ctx.send(embed=embed)
                            await ctx.message.delete()


                    elif ctx.message.attachments: #Checks if there is an image
                        for attachment in ctx.message.attachments:
                            if len(args) == 1: 
                                embed=discord.Embed(title=f"+Rep", description=f"{member} has been Repped!", color=0x00ffcc)
                                embed.add_field(name="Amount", value=f"${money_input}", inline=False)
                                embed.add_field(name="Proof", value=f"{attachment.url}", inline=False)
                                embed.set_thumbnail(url=f"{attachment.url}")
                                embed.add_field(name="User ID", value=f"Received: {member}, {member.id}\n Sent: {ctx.author}, {ctx.author.id}", inline=False)
                                embed.set_footer(text="Any issues dm Beetlemadooda#0955")
                                await ctx.send(embed=embed)
                                await ctx.message.delete()


                    else: #Checks if its a normal rep field.
                        embed=discord.Embed(title=f"No Proof!", description=f"{ctx.author.mention} You must include either a Gayzo, Imgur or Discord Image", color=0xf1c40f)
                        embed.set_thumbnail(url="https://i.pinimg.com/originals/84/c0/1a/84c01aa60d96039f4aae384f59e0b6db.jpg")
                        embed.add_field(name="Syntax", value="+rep @user (Amount) (Gayzo, Imgur or discord image)", inline=False)
                        embed.add_field(name="Example", value=f"+rep {ctx.author} $25 https://gyazo.com/example", inline=False)
                        embed.set_footer(text="Any issues dm Beetlemadooda#0955")
                        await ctx.send(embed=embed, delete_after=10.0)
                        await ctx.message.delete()


                    for i in range(0,len(Json_Items)): #It doesn't exist
                        for x in Json_Items[i]:
                            if int(x) == int(member.id):
                                Json_Items[i][x]['Total_Deals_Amount'] = int(Json_Items[i][x]['Total_Deals_Amount']) + int(money_input)
                                Json_Items[i][x]['Total_Deals_Completed'] = int(Json_Items[i][x]['Total_Deals_Completed']) + int(1)
                                json.dump(Json_Items, open("./all_user_rep.json", "w"), indent=1)
                                user_exists_in_json = True
                    

                    if user_exists_in_json == False:
                        dict1 ={
                            member.id: {
                                "Discord_Name": member.name,
                                "Total_Deals_Amount": money_input,
                                "Total_Deals_Completed": "1"
                            }}
                        Json_Items.append(dict1)
                        json.dump(Json_Items, open("./all_user_rep.json", "w"), indent=1)
        else:
            return

#------------------------------------------------------------------------------------------------------------------------------
# +rep_add @user
#------------------------------------------------------------------------------------------------------------------------------
temp_var_3 = False
@bot.command()
async def add(ctx, member:discord.User, a:int, b:int):
    channel = bot.get_channel(845821666159230976)
    global temp_var_3
    temp_var_3 = False
    if ctx.channel.id == channel.id:
        for i in range(0,len(Json_Items)): #It doesn't exist
            for x in Json_Items[i]:
                if int(x) == int(member.id):
                    Json_Items[i][x]['Total_Deals_Completed'] = int(Json_Items[i][x]['Total_Deals_Completed']) + int(a)
                    Json_Items[i][x]['Total_Deals_Amount'] = int(Json_Items[i][x]['Total_Deals_Amount']) + int(b)
                    json.dump(Json_Items, open("./all_user_rep.json", "w"), indent=1)
                    total_money = Json_Items[i][x]['Total_Deals_Amount']
                    total_deals = Json_Items[i][x]['Total_Deals_Completed'] 
                    embed=discord.Embed(title=f"Check", description=f"This is {member} rep!", color=0xe74c3c)
                    embed.add_field(name="Total Deals", value=f"{member.mention} has completed a total of {total_deals} rep!", inline=False)
                    embed.add_field(name="Total Amount", value=f"{member.mention} has an amount of ${total_money}!", inline=False)
                    embed.set_footer(text="Any issues dm Beetlemadooda#0955")
                    await ctx.send(embed=embed, delete_after=20.0)
                    await ctx.send(f"Adding rep to {member}!", delete_after=20.0)
                    await ctx.message.delete()
                    temp_var_3 = True
        if temp_var_3 == False:
            dict1 ={
                member.id: {
                    "Discord_Name": member.name,
                    "Total_Deals_Amount": a,
                    "Total_Deals_Completed": b
                }}
            Json_Items.append(dict1)
            json.dump(Json_Items, open("./all_user_rep.json", "w"), indent=1)
            embed=discord.Embed(title=f"Check", description=f"This is {member} rep!", color=0xe74c3c)
            embed.add_field(name="Total Deals", value=f"{member.mention} has completed a total of {b} rep!", inline=False)
            embed.add_field(name="Total Amount", value=f"{member.mention} has an amount of ${a}!", inline=False)
            embed.set_footer(text="Any issues dm Beetlemadooda#0955")
            await ctx.send(embed=embed, delete_after=20.0)
            await ctx.send(f"Adding rep to {member}!", delete_after=20.0)
            await ctx.message.delete()

    else:
        embed=discord.Embed(title=f"ERROR", description=f"{ctx.author.mention} You do not have access to this command!", color=0xf1c40f)
        await ctx.send(embed=embed)
        await ctx.message.delete()

#------------------------------------------------------------------------------------------------------------------------------
# +rep_take @user
#------------------------------------------------------------------------------------------------------------------------------
temp_var_2 = False
@bot.command()
async def remove(ctx, member:discord.User, a:int, b:int):
    global temp_var_2
    channel = bot.get_channel(845821666159230976)
    temp_var_2 = False
    if ctx.channel.id == channel.id:
        for i in range(0,len(Json_Items)): #It doesn't exist
            for x in Json_Items[i]:
                if int(x) == int(member.id):
                    if a > Json_Items[i][x]['Total_Deals_Completed'] or b > Json_Items[i][x]['Total_Deals_Amount']:
                        await ctx.send(f"{ctx.author.mention} bruh ur staff. Either msg the goat Beetle or like don't give the person to much rep. Check the user, then remove.\n"
                        "Do +check the user, then type +remove @user (Rep Amount) (Money Amount)")
                        temp_var_2 = True
        if temp_var_2 == False:
            for i in range(0,len(Json_Items)): #It doesn't exist
                for x in Json_Items[i]:
                    if int(x) == int(member.id):
                        Json_Items[i][x]['Total_Deals_Completed'] = int(Json_Items[i][x]['Total_Deals_Completed']) - int(a)
                        Json_Items[i][x]['Total_Deals_Amount'] = int(Json_Items[i][x]['Total_Deals_Amount']) - int(b)
                        json.dump(Json_Items, open("./all_user_rep.json", "w"), indent=1)
                        total_money = Json_Items[i][x]['Total_Deals_Amount']
                        total_deals = Json_Items[i][x]['Total_Deals_Completed'] 
                        embed=discord.Embed(title=f"Check", description=f"This is {member} rep!", color=0xe74c3c)
                        embed.add_field(name="Total Deals", value=f"{member.mention} has completed a total of {total_deals} rep!", inline=False)
                        embed.add_field(name="Total Amount", value=f"{member.mention} has an amount of ${total_money}!", inline=False)
                        embed.set_footer(text="Any issues dm Beetlemadooda#0955")
                        await ctx.send(embed=embed, delete_after=20.0)
                        await ctx.send(f"Removing rep from {member}!", delete_after=20.0)
                        await ctx.message.delete()


                    # Json_Items[i][x]['Total_Deals_Completed'] = int(Json_Items[i][x]['Total_Deals_Completed']) - int(a)
                    
    else:
        embed=discord.Embed(title=f"ERROR", description=f"{ctx.author.mention} You do not have access to this command!", color=0xf1c40f)
        await ctx.send(embed=embed)
        await ctx.message.delete()
    
#------------------------------------------------------------------------------------------------------------------------------
# Remove all messages that don't start with +
#------------------------------------------------------------------------------------------------------------------------------
@bot.listen()
async def on_message(message):
    channel = bot.get_channel(845567167251742740)
    if message.author == bot.user:
        return
    if (message.content.startswith("+") == False and message.channel.id == channel.id):
        await message.delete()
        embed=discord.Embed(title=f"Error", description=f"{message.author.mention} Your message did not start with '+' (This is the REP channel!)", color=0xe74c3c)
        embed.add_field(name="syntax", value="+rep @user (Amount) (Gayzo, Ingur or Discord Attachement Image.)", inline=False)
        embed.add_field(name="Example", value=f"+rep {message.author} $25 https://gyazo.com/example", inline=False)
        embed.set_footer(text="Any issues dm Beetlemadooda#0955")
        await channel.send(embed=embed, delete_after=5.0)

#------------------------------------------------------------------------------------------------------------------------------    
# Error Handling 
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed=discord.Embed(title=f"Error", description=f"{ctx.author} You have used the rep command incorrectly! Please follow the syntax below.", color=0xf1c40f)
        embed.add_field(name="syntax", value="+rep @user (Amount) (Imgur, Gayzo or Discord Attachement)", inline=False)
        embed.add_field(name="Example", value=f"+rep {ctx.author} $25 https://gyazo.com/example", inline=False)
        embed.set_footer(text="Any issues dm Beetlemadooda#0955")
        await ctx.send(embed=embed, delete_after=10.0)
        await ctx.message.delete()
    elif isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title=f"ERROR", description=f"{ctx.author.mention} You are not entering the command in right! Please do +help", color=0xf1c40f)
        await ctx.send(embed=embed, delete_after=10.0)
        await ctx.message.delete()
    elif isinstance(error, commands.MissingPermissions):
        embed=discord.Embed(title=f"Invalid Perms", description=f"{ctx.author.mention} You do not have perms to this command!", color=0xf1c40f)
        embed.set_footer(text="Any issues dm Beetlemadooda#0955")
        await ctx.send(embed=embed, delete_after=10.0)
        await ctx.message.delete()
    elif isinstance(error, commands.UserNotFound):
        embed=discord.Embed(title=f"Wrong User", description=f"{ctx.author.mention} The user you are trying to rep is not in the server!", color=0xf1c40f)
        embed.add_field(name="syntax", value="+rep @user (Amount) (Gayzo, Ingur or Discord Attachement Image.)", inline=False)
        embed.add_field(name="Example", value=f"+rep {ctx.author} $25 https://gyazo.com/example", inline=False)
        embed.set_footer(text="Any issues dm Beetlemadooda#0955")
        await ctx.send(embed=embed, delete_after=10.0)
        await ctx.message.delete()        
    else:
        embed=discord.Embed(title=f"ERROR", description=f"{ctx.author.mention} You have raised a weird error! Please contact Beetlemadooda#0955", color=0xf1c40f)
        embed.add_field(name="Error for Beetle", value=f"{error}", inline=False)
        await ctx.send(embed=embed, delete_after=60.0)
        await ctx.message.delete()
bot.run(TOKEN)   


# Notes:
# Make it so proof is NECCESARY! 
# Done
# Prints the staff_ping check in a specific channel.
# Done
# Delete any rep deals that are over $2000, and give the user bannedfromtrading
# Done


# Things Done:
# - Imports
# - Globals
# - Json
# - Help Command
# - Deleting messages
# - +Check command
# - +rep @user command
# - +rep add @user command
# - +rep take @user command
# - Error handling

# Things to do:

