import discord
from discord.ext import commands

from asyncKirara import Kirara
from datetime import datetime


class Deresute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def card(self, ctx, name, rarity, release):
        """Find a card's information from the database"""
        client = Kirara()
        raw_rarity = rarity.replace('+', '')    
        card_id = await client.get_id('card_t', f' {name}', raw_rarity, int(release))
        if '+' in rarity:
            card_id += 1
        idol = await client.get_card(card_id, en_translate=True)
        url = f"https://starlight.kirara.ca/card/{idol.card_id}"
        
        embed=discord.Embed(title=f"[{idol.title}]{idol.conventional}",
        url=url, color=self.bot.attributes.get(idol.type))

        embed.set_thumbnail(url=idol.icon)
        if idol.has_spread:
            embed.set_image(url=idol.spread)

        embed.add_field(name=f"Lead Skill: {idol.lead_skill.name}",
        value=idol.lead_skill.en_explain, inline=False)

        embed.add_field(name='Vocal', value=idol.max_vocal, inline=True)
        embed.add_field(name='Dance', value=idol.max_dance, inline=True)
        embed.add_field(name='Visual', value=idol.max_visual, inline=True)
        embed.add_field(name='HP', value=idol.max_hp, inline=True)
        embed.add_field(name=f"Skill: {idol.skill.skill_type}",
        value=idol.skill.en_explain, inline=False)

        embed.set_footer(text=f"Card ID: {idol.card_id}")

        
        await ctx.send(embed=embed)
        await client.close()

    @commands.command()
    async def cards(self, ctx, name, rarity):
        """Lists cards in a specific rarity that an idol has"""
        client = Kirara()
        id_list = await client.get_id('card_t', f' {name}', rarity)
        card_list = await client.get_cards(id_list, en_translate=True)

        embed = discord.Embed(title=f'{card_list[0].conventional}',
        color=self.bot.attributes.get(card_list[0].type))

        for card in card_list:
            embed.add_field(name=f'[{card.title}] {card.conventional}',
            value=f'Vocal: {card.max_vocal}\nDance: {card.max_dance}\n' +
            f'Visual: {card.max_visual}\nHP: {card.max_hp}')
        
        await ctx.send(embed=embed)
        await client.close()

    @commands.command()
    async def event(self, ctx):
        """Show information about the current event 
        (NOTE: Will only work with specfic events)"""
        client = Kirara()
        event = await client.get_now('event', en_translate=False)
        current_event = event[0]

        currently = datetime.utcnow().timestamp()
        remaining = ((current_event.end_date + 32400) - currently) - 3600
        hours, remainder = divmod(remaining, 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        cards = await client.get_id('card_t', current_event.name, is_title=True)
        event_cards = await client.get_cards(cards, en_translate=True)

        embed=discord.Embed(title=current_event.name,
        description=f'Time Left: {days} Days, {hours} hours' +
        f' {minutes} minutes, {round(seconds)} seconds', color=0xd629c9)
        embed.add_field(name='Event Cards', value='='*30)

        for card in event_cards:
            embed.add_field(name=f'[{card.title}] {card.conventional}',
            value=f'Lead Skill: {card.lead_skill.en_explain}',
            inline=False)

        await ctx.send(embed=embed)        

def setup(bot):
    bot.add_cog(Deresute(bot))
