import discord
import asyncio
import random
import functools
import itertools
import math
import os
from discord.ext import commands

#접두사
bot = commands.Bot(command_prefix="다온아 ")

#로그인
@bot.event
async def on_ready():
    print('Loggend in Bot: ', bot.user.name)
    print('Bot id: ', bot.user.id)
    print('connection was succesful!')
    print('=' * 30)

#명령어 보기
@bot.command()
async def 명령어(ctx):
  embed=discord.Embed(title="명령어 모음이에요!", description="명령어 앞에 '다온아'를 붙이고 말해주세요 :)", color=0xC4DBF9)
  embed.set_thumbnail(url="https://drive.google.com/uc?id=1j1a9HIc2aN5dvApQ8m7SmLpWBB2Dnbwv")
  embed.add_field(name="명령어", value="명령어를 보여줘요.", inline=False)
  embed.add_field(name="그림합작", value="그림합작 정보를 알려줘요.", inline=False)
  embed.add_field(name="소설합작", value="소설합작 정보를 알려줘요.", inline=False)
  embed.set_footer(text = f"Bot made by 나르디#5829", icon_url = ctx.message.author.avatar_url)
  await ctx.send(embed=embed)

#그림합작 주제 확인
@bot.command()
async def 그림합작(ctx):
  embed=discord.Embed(title="3차 합작", description="주제: 추석", color=0xC4DBF9)
  embed.add_field(name="양식", value="SD전신", inline=False)
  embed.add_field(name="규격", value="png파일, 가로세로 1000px이상", inline=False)
  embed.add_field(name="마감일", value="9월 25일(일)", inline=False)
  embed.add_field(name="제출", value="디엠 또는 메일(narrator421@naver.com)", inline=False)
  embed.set_footer(text = f"Bot made by 나르디#5829", icon_url = ctx.message.author.avatar_url)
  await ctx.send(embed=embed)

#소설합작 주제 확인
@bot.command()
async def 소설합작(ctx):
  embed=discord.Embed(title="3차 합작", description="주제: 추석", color=0xC4DBF9)
  embed.add_field(name="양식", value="단편 소설(약 5000자)", inline=False)
  embed.add_field(name="장르", value="자유", inline=False)
  embed.add_field(name="마감일", value="9월 25일(일)", inline=False)
  embed.add_field(name="제출", value="디엠 또는 메일(narrator421@naver.com)", inline=False)
  embed.set_footer(text = f"Bot made by 나르디#5829", icon_url = ctx.message.author.avatar_url)
  await ctx.send(embed=embed)

#합작용 주제 추천하기
@bot.command()
async def 주제(ctx, *, text):
  await ctx.send(text+"! 멋진 주제 추천 감사합니다 :)")

#합작용 주제 뽑기
@bot.command()
async def 주제뽑기(ctx, *, text):
  #주제
  topic = ["꿈"]
  randomT = random.randrange(0,len(topic))
  #장르
  genre = ["로맨스", "로판" ,"판타지", "현판", "스릴러(미스터리, 추리 포함)","자유"]
  randomG = random.randrange(0,len(genre))
  #데포르메
  deforme = ["SD", "MD" ,"LD"]
  randomD = random.randrange(0,len(deforme))
  #사이즈
  size = ["두상", "흉상" ,"반신","전신"]
  randomS = random.randrange(0,len(size))
  #임베드
  embed=discord.Embed(title=text+"차 합작", description="주제 추첨 결과입니다!", color=0xC4DBF9)
  embed.add_field(name="뽑힌 주제", value=topic[randomT], inline=False)
  embed.add_field(name="추천된 주제", value="꿈, 추석, 자유, 가을, 단풍", inline=False)
  embed.add_field(name="소설 장르", value=genre[randomG], inline=False)
  embed.add_field(name="그림 양식", value=deforme[randomD]+","+size[randomS], inline=False)
  embed.set_footer(text = f"Bot made by 나르디#5829", icon_url = ctx.message.author.avatar_url)
  await ctx.send(embed=embed)




'''
@bot.command(aliases=['나왔어','좋은아침','좋은점심','좋은저녁','나왔어!','좋은아침!','좋은점심!','좋은저녁!','안녕!'])
async def 안녕(ctx):
  await ctx.send("{}님, 안녕하세요".format(ctx.author.mention))

@bot.command(aliases=['이따봐','내일봐','이따보자'])
async def 내일보자(ctx):
  await ctx.send("{}님, 안녕히가세요!".format(ctx.author.mention))

@bot.command(aliases=['따라해봐','이거해봐','따라하기','따라해봐!'])
async def 따라해(ctx, *, text):
    await ctx.send(text)

@bot.command(aliases=['주사위굴려줘'])
async def 주사위(ctx):
    randnum = random.randint(1, 6)
    msg = await ctx.send("🎲주사위를 굴립니다...")
    await msg.edit(content=f'🎲주사위 결과는 {randnum}입니다!')

@bot.command(aliases=['도배해줘'])
async def 도배(ctx, *, text):
  await ctx.send(text*300)

@bot.command(aliases=['보석'])
async def 보석캐기(ctx):
    minerals = ['다이아몬드', '루비', '에메랄드', '자수정', '철', '석탄']
    weights = [1, 3, 6, 15, 25, 50]
    results = random.choices(minerals, weights=weights, k=5)
    embed=discord.Embed(title="다음 광물들을 획득하였습니다!", description=('``'+'``, ``'.join(results) + '``'), color=0xF0F8FF)
    await ctx.send(embed=embed)

@bot.command()
async def 추방(ctx, nickname: discord.Member):
	await nickname.kick()
	await ctx.send(f"{nickname} 님을 추방했습니다.")

@bot.command()
async def 차단(ctx, nickname: discord.Member):
	await nickname.ban()
	await ctx.send(f"{nickname} 님을 차단했습니다.")

@bot.command()
async def 해제(ctx, nickname: str):
    ban_entry = await ctx.guild.bans()
    for users in ban_entry:
        if nickname == users.user.name:
            forgive_user = users.user
            await ctx.guild.unban(forgive_user)
            return await ctx.send(f"{nickname} 님이 차단 해제되었습니다.")
    return await ctx.send(f"{nickname}님은 차단 목록에 없습니다.")

def make_dir(directory_name):
    try:
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
    except OSError:
        print('Error: makedirs()')

def add_result(directory_name, user_name, result):
    file_path = directory_name + '/' + user_name + '.txt'
    if os.path.exists(file_path):
        with open(file_path, 'a', encoding='UTF-8') as f:
            f.write(result)
    else:
        with open(file_path, 'w', encoding='UTF-8') as f:
            f.write(result)

@bot.command()
async def 가위바위보(ctx, user: str):
    rps_table = ['가위', '바위', '보']
    bot = random.choice(rps_table)
    result = rps_table.index(user) - rps_table.index(bot)
    if result == 0:
        result_text = f'``{user} vs {bot}`` 비김\n'
        await ctx.send(f'``{user} vs {bot}`` 비겼어요..!')
    elif result == 1 or result == -2:
        result_text = f'``{user} vs {bot}`` 승리!\n'
        await ctx.send(f'``{user} vs {bot}`` 제가 졌어요...')
    else:
        result_text = f'``{user} vs {bot}`` 패배...\n'
        await ctx.send(f'``{user} vs {bot}`` 제가 이겼어요!')
        
    directory_name = "rps_result"
    make_dir(directory_name)
    add_result(directory_name, str(ctx.author), result_text)

@bot.command()
async def 전적(ctx):
    user_name = str(ctx.author)
    file_path = "rps_result/" + user_name + ".txt"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="UTF-8") as f:
            result = f.read()
        await ctx.send(f'{ctx.author}님의 가위바위보 게임 전적입니다.\n==============================\n' + result)
    else:
        await ctx.send(f'{ctx.author}님의 가위바위보 전적이 존재하지 않습니다.')

@bot.command()
async def 릴레이소설(ctx):
  novel = ["유난히 달이 밝던 어느 날이었다.","그녀는 나를 보며 말했다.","나는 여기서 뭘 하고 있는 걸까.","눈을 떠 보니 이곳이었다.","머리가 아프다.","저 앞에 무언가가 보인다.","맑고 화창한 날이다.","그날은, 비가 왔었다.","그날, 그녀는 나를 떠났다.","그날, 그는 나를 떠났다.","얼마나 기다렸을까.","벌써 며칠이 지났다.","더 이상 아무 것도 하고 싶지 않다.","나는 뜨거운 태양 빛에 눈살을 찌푸렸다.","저 멀리 그녀가 보인다.","저 멀리 그가 보인다."]
  randomNum = random.randrange(0,len(novel))
  await ctx.send(novel[randomNum])

@bot.command(aliases=['나랑놀자','심심해','놀아줘'])
async def 놀자(ctx):
  embed=discord.Embed(title="그럼 저랑 같이 놀아요!", description="다양한 게임들이 있답니다.", color=0xFFCAD7)
  embed.set_thumbnail(url="https://drive.google.com/uc?id=1YfMHgJE6LY0V7OB43sOBCpdD-ShTyh5W")
  embed.add_field(name="가위바위보", value="저랑 가위바위보해요!", inline=False)
  embed.set_footer(text = f"Bot made by 쨍₍ᐢ..ᐢ₎⊹#9646", icon_url = ctx.message.author.avatar_url)
  await ctx.send(embed=embed)

@bot.command(aliases=['문제','문제풀기'])
async def 문제풀래(ctx):
    timeout = 5 #// 기다릴 시간 정하기
    send_message = await ctx.send(f'A의 나이는 B의 나이의 3배입니다.₩nB의 나이에 제곱을 하면 A의 나이의 5배가 됩니다.₩nA의 나이는 몆 살일까요?{timeout}초간 기다립니다!')

    def check(m): # check 메서드 정의
        return m.author == ctx.message.author and m.channel == ctx.message.channel # 같은 채널에서 같은 메시지를 보낸 사람의 이벤트를 체크

    try: # 5초간 기다림
    	# 이벤트 입력 시 앞의 'on_'은 떼고 입력함
        msg = await bot.wait_for('message', check=check, timeout=timeout)
    except asyncio.TimeoutError: #// 5초가 지나면 TimeoutError 발생
        await ctx.send(f'시간초과 입니다...({timeout}초)')
    else: #// 5초 안에 'on_message' 이벤트 수신 시
        await ctx.send(f'{msg.content}메시지를 {timeout}초 안에 입력하셨습니다!')
'''

bot.run('MTAxOTU5ODU1Mzg2MzE1OTkyOQ.GRbKm9.hqjt-ILqOnibAEjeB51sYHVwAgb6MFpEDrQbm4')
