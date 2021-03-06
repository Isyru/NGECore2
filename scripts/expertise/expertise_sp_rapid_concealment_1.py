import sys

def addExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'spy_1a':
		return

	actor.addSkill('expertise_sp_rapid_concealment_1')

	actor.addSkillMod('expertise_cooldown_line_sp_smoke', 30)
	actor.addSkillMod('expertise_cooldown_line_sp_burst_shadows', 30)

	addAbilities(core, actor, player)

	return

def removeExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'spy_1a':
		return

	actor.removeSkill('expertise_sp_rapid_concealment_1')

	actor.removeSkillMod('expertise_cooldown_line_sp_smoke', 30)
	actor.removeSkillMod('expertise_cooldown_line_sp_burst_shadows', 30)

	removeAbilities(core, actor, player)

	return

# this checks what abilities the player gets by level, need to also call this on level-up
def addAbilities(core, actor, player):


	return

def removeAbilities(core, actor, player):


	return
