"""Constants taken from the game and PathOfBuilding."""

# Collections of game objects.
TREE_OFFSET = 7  # Skill tree node data is offset 7 bytes from the start.
BANDITS = ("Kraityn", "Alira", "Oak")
CLASS_NAMES = ("Duelist", "Marauder", "Ranger", "Scion", "Shadow", "Templar", "Witch")
ASCENDANCY_NAMES = ("Ascendant", "Assassin", "Berserker", "Champion", "Chieftain", "Deadeye", "Elementalist",
                    "Gladiator", "Guardian", "Hierophant", "Inquisitor", "Juggernaut", "Necromancer", "Occultist",
                    "Pathfinder", "Raider", "Saboteur", "Slayer", "Trickster")

# Taken from DefaultMonsterStats.dat
MONSTER_DAMAGE_TABLE = (5, 6, 6, 7, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 23, 24, 26, 28, 30, 32, 34, 36,
                        39, 41, 44, 47, 50, 53, 56, 59, 63, 67, 71, 75, 80, 84, 89, 94, 100, 106, 112, 118, 125, 131,
                        139, 147, 155, 163, 172, 181, 191, 202, 212, 224, 236, 248, 262, 275, 290, 305, 321, 338, 355,
                        374, 393, 413, 434, 456, 480, 504, 530, 556, 584, 614, 645, 677, 711, 746, 783, 822, 862, 905,
                        949, 996, 1045, 1096, 1149, 1205, 1264, 1325, 1390, 1457, 1527, 1601, 1678, 1758)
MONSTER_LIFE_TABLE = (15, 18, 21, 25, 29, 33, 38, 43, 49, 55, 61, 68, 76, 85, 94, 104, 114, 126, 138, 152, 166, 182,
                      199, 217, 236, 257, 280, 304, 331, 359, 389, 422, 456, 494, 534, 577, 624, 673, 726, 783, 844,
                      910, 980, 1055, 1135, 1221, 1313, 1411, 1516, 1629, 1749, 1878, 2015, 2162, 2319, 2486, 2665,
                      2857, 3061, 3279, 3512, 3760, 4025, 4308, 4610, 4932, 5276, 5642, 6033, 6449, 6894, 7367, 7872,
                      8410, 8984, 9595, 10246, 10940, 11679, 12466, 13304, 14198, 15149, 16161, 17240, 18388, 19610,
                      20911, 22296, 23770, 25338, 27007, 28784, 30673, 32684, 34823, 37098, 39519, 42093, 44831)

# Mapping between PathOfBuilding's export format and this API.
CONFIG_MAP = {
    "resistancePenalty": "resistance_penalty",
    "enemyLevel": "enemy_level",
    "enemyPhysicalHit": "enemy_physical_hit_damage",
    "detonateDeadCorpseLife": "detonate_dead_corpse_life",
    "conditionStationary": "is_stationary",
    "conditionMoving": "is_moving",
    "conditionFullLife": "on_full_life",
    "conditionLowLife": "on_low_life",
    "conditionFullEnergyShield": "on_full_energy_shield",
    "conditionHaveEnergyShield": "has_energy_shield",
    "minionsConditionFullLife": "minions_on_full_life",
    "igniteMode": "ignite_mode",
    "aspectOfTheAvianAviansMight": "aspect_of_the_avian_avians_might",
    "aspectOfTheAvianAviansFlight": "aspect_of_the_avian_avians_flight",
    "aspectOfTheCatCatsStealth": "aspect_of_the_cat_cats_stealth",
    "aspectOfTheCatCatsAgility": "aspect_of_the_cat_cats_agility",
    "overrideCrabBarriers": "override_crab_barriers",
    "aspectOfTheSpiderWebStacks": "aspect_of_the_spider_web_stacks",
    "darkPactSkeletonLife": "dark_pact_skeleton_life",
    "iceNovaCastOnFrostbolt": "ice_nova_cast_on_frostbolt",
    "innervateInnervation": "innervate_innervation",
    "raiseSpectreSpectreLevel": "raise_spectres_spectre_level",
    "siphoningTrapAffectedEnemies": "siphoning_trap_affected_enemies",
    "raiseSpectreEnableCurses": "raise_spectres_enable_curses",
    "raiseSpectreBladeVortexBladeCount": "raise_spectres_blade_vortex_blade_count",
    "summonLightningGolemEnableWrath": "summon_lightning_golem_enable_wrath",
    "vortexCastOnFrostbolt": "vortex_cast_on_frostbolt",
    "enemyHasPhysicalReduction": "enemy_physical_reduction",
    "enemyIsHexproof": "enemy_hexproof",
    "enemyHasLessCurseEffectOnSelf": "less_curse_effect",
    "enemyCanAvoidPoisonBlindBleed": "enemy_avoid_poison_blind_bleed",
    "enemyHasResistances": "enemy_resistances",
    "playerHasElementalEquilibrium": "elemental_equilibrium",
    "playerCannotLeech": "no_leech",
    "playerGainsReducedFlaskCharges": "reduced_flask_charges",
    "playerHasMinusMaxResist": "minus_max_resists",
    "playerHasLessAreaOfEffect": "less_aoe",
    "enemyCanAvoidStatusAilment": "enemy_avoid_status_ailment",
    "enemyHasIncreasedAccuracy": "enemy_increased_accuracy",
    "playerHasLessArmourandBlock": "less_armour_block",
    "playerHasPointBlank": "point_blank",
    "playerHasLessLifeESRecovery": "less_recovery",
    "playerCannotRegenLifeManaEnergyShield": "no_regen",
    "enemyTakesReducedExtraCritDamage": "enemy_takes_reduced_extra_crit_damage",
    "playerCursedWithAssassinsMark": "curse_assassins_mark",
    "playerCursedWithConductivity": "curse_conductivity",
    "playerCursedWithDespair": "curse_despair",
    "playerCursedWithElementalWeakness": "curse_elemental_weakness",
    "playerCursedWithEnfeeble": "curse_enfeeble",
    "playerCursedWithFlammability": "curse_flammability",
    "playerCursedWithFrostbite": "curse_frostbite",
    "playerCursedWithPoachersMark": "curse_poachers_mark",
    "playerCursedWithProjectileWeakness": "curse_projectile_weakness",
    "playerCursedWithPunishment": "curse_punishment",
    "playerCursedWithTemporalChains": "curse_temporal_chains",
    "playerCursedWithVulnerability": "curse_vulnerability",
    "playerCursedWithWarlordsMark": "curse_warlords_mark",
    "usePowerCharges": "use_power_charges",
    "overridePowerCharges": "max_power_charges",
    "useFrenzyCharges": "use_frenzy_charges",
    "overrideFrenzyCharges": "max_frenzy_charges",
    "useEnduranceCharges": "use_endurance_charges",
    "overrideEnduranceCharges": "max_endurance_charges",
    "useSiphoningCharges": "use_siphoning_charges",
    "overrideSiphoningCharges": "max_siphoning_charges",
    "minionsUsePowerCharges": "minions_use_power_charges",
    "minionsUseFrenzyCharges": "minions_use_frenzy_charges",
    "minionsUseEnduranceCharges": "minions_use_endurance_charges",
    "buffOnslaught": "onslaught",
    "buffUnholyMight": "unholy_might",
    "buffPhasing": "phasing",
    "buffFortify": "fortify",
    "buffTailwind": "tailwind",
    "buffAdrenaline": "adrenaline",
    "multiplierRage": "rage",
    "conditionLeeching": "leeching",
    "conditionUsingFlask": "using_flask",
    "conditionHaveTotem": "has_totem",
    "conditionOnConsecratedGround": "on_consecrated_ground",
    "conditionOnBurningGround": "on_burning_ground",
    "conditionOnChilledGround": "on_chilled_ground",
    "conditionOnShockedGround": "on_shocked_ground",
    "conditionBurning": "burning",
    "conditionIgnited": "ignited",
    "conditionChilled": "chilled",
    "conditionFrozen": "frozen",
    "conditionShocked": "shocked",
    "conditionBleeding": "bleeding",
    "conditionPoisoned": "poisoned",
    "multiplierPoisonOnSelf": "number_of_poison_stacks",
    "conditionOnlyOneNearbyEnemy": "only_one_nearby_enemy",
    "conditionHitRecently": "hit_recently",
    "conditionCritRecently": "crit_recently",
    "conditionNonCritRecently": "non_crit_recently",
    "conditionKilledRecently": "killed_recently",
    "multiplierKilledRecently": "number_of_enemies_killed_recently",
    "conditionTotemsKilledRecently": "totems_killed_recently",
    "multiplierTotemsKilledRecently": "number_of_totems_killed_recently",
    "conditionMinionsKilledRecently": "minions_killed_recently",
    "multiplierMinionsKilledRecently": "number_of_minions_killed_recently",
    "conditionKilledAffectedByDoT": "killed_affected_by_dot",
    "multiplierShockedEnemyKilledRecently": "number_of_shocked_enemies_killed_recently",
    "conditionFrozenEnemyRecently": "frozen_enemy_recently",
    "conditionShatteredEnemyRecently": "shattered_enemy_recently",
    "conditionIgnitedEnemyRecently": "ignited_enemy_recently",
    "conditionShockedEnemyRecently": "shocked_enemy_recently",
    "multiplierPoisonAppliedRecently": "number_of_poisons_applied_recently",
    "conditionBeenHitRecently": "been_hit_recently",
    "conditionBeenCritRecently": "been_crit_recently",
    "conditionBeenSavageHitRecently": "been_savage_hit_recently",
    "conditionHitByFireDamageRecently": "hit_by_fire_damage_recently",
    "conditionHitByColdDamageRecently": "hit_by_cold_damage_recently",
    "conditionHitByLightningDamageRecently": "hit_by_lightning_damage_recently",
    "conditionBlockedRecently": "blocked_recently",
    "conditionBlockedAttackRecently": "blocked_attack_recently",
    "conditionBlockedSpellRecently": "blocked_spell_recently",
    "conditionEnergyShieldRechargeRecently": "energy_shield_recharge_started_recently",
    "buffPendulum": "pendulum_of_destruction",
    "buffConflux": "elemental_conflux",
    "buffBastionOfHope": "bastion_of_hope",
    "buffHerEmbrace": "her_embrace",
    "conditionUsedSkillRecently": "used_skill_recently",
    "multiplierSkillUsedRecently": "number_of_skills_used_recently",
    "conditionAttackedRecently": "attacked_recently",
    "conditionCastSpellRecently": "cast_spell_recently",
    "conditionUsedFireSkillRecently": "used_fire_skill_recently",
    "conditionUsedColdSkillRecently": "used_cold_skill_recently",
    "conditionUsedMinionSkillRecently": "used_minion_skill_recently",
    "conditionUsedMovementSkillRecently": "used_movement_skill_recently",
    "conditionUsedVaalSkillRecently": "used_vaal_skill_recently",
    "conditionUsedWarcryRecently": "used_warcry_recently",
    "multiplierMineDetonatedRecently": "number_of_mines_detonated_recently",
    "multiplierTrapTriggeredRecently": "number_of_traps_triggered_recently",
    "conditionConsumedCorpseRecently": "consumed_corpses_recently",
    "multiplierCorpseConsumedRecently": "number_of_corpses_consumed_recently",
    "conditionTauntedEnemyRecently": "taunted_enemy_recently",
    "conditionBlockedHitFromUniqueEnemyInPast10Sec": "blocked_hit_from_unique_enemy_in_past_ten_seconds",
    "critChanceLucky": "lucky_crits",
    "skillChainCount": "number_of_times_skill_has_chained",
    "projectileDistance": "projectile_distance",
    "conditionAtCloseRange": "enemy_in_close_range",
    "conditionEnemyMoving": "enemy_moving",
    "conditionEnemyFullLife": "enemy_on_full_life",
    "conditionEnemyLowLife": "enemy_on_low_life",
    "conditionEnemyCursed": "enemy_cursed",
    "conditionEnemyBleeding": "enemy_bleeding",
    "conditionEnemyPoisoned": "enemy_poisoned",
    "multiplierPoisonOnEnemy": "enemy_number_of_poison_stacks",
    "conditionEnemyMaimed": "enemy_maimed",
    "conditionEnemyHindered": "enemy_hindered",
    "conditionEnemyBlinded": "enemy_blinded",
    "conditionEnemyTaunted": "enemy_taunted",
    "conditionEnemyBurning": "enemy_burning",
    "conditionEnemyIgnited": "enemy_ignited",
    "conditionEnemyChilled": "enemy_chilled",
    "conditionEnemyFrozen": "enemy_frozen",
    "conditionEnemyShocked": "enemy_shocked",
    "multiplierFreezeShockIgniteOnEnemy": "enemy_number_of_freeze_shock_ignite",
    "conditionEnemyIntimidated": "enemy_intimidated",
    "conditionEnemyCoveredInAsh": "enemy_covered_in_ash",
    "conditionEnemyRareOrUnique": "enemy_rare_or_unique",
    "enemyIsBoss": "enemy_boss",
    "enemyPhysicalReduction": "enemy_physical_reduction",
    "enemyFireResist": "enemy_fire_resist",
    "enemyColdResist": "enemy_cold_resist",
    "enemyLightningResist": "enemy_lightning_resist",
    "enemyChaosResist": "enemy_chaos_resist",
    "enemyConditionHitByFireDamage": "enemy_hit_by_fire_damage",
    "enemyConditionHitByColdDamage": "enemy_hit_by_cold_damage",
    "enemyConditionHitByLightningDamage": "enemy_hit_by_lightning_damage",
    "EEIgnoreHitDamage": "elemental_equilibrium_ignore_hit_damage"}
STATS_MAP = {
    "AverageHit": "average_hit",
    "AverageDamage": "average_damage",
    "Speed": "cast_speed",
    "HitSpeed": "attack_speed",
    "TrapThrowingTime": "trap_throwing_speed",
    "TrapCooldown": "trap_cooldown",
    "MineLayingTime": "mine_laying_speed",
    "TotemPlacementTime": "totem_placement_speed",
    "PreEffectiveCritChance": "pre_effective_crit_chance",
    "CritChance": "crit_chance",
    "CritMultiplier": "crit_multiplier",
    "HitChance": "hit_chance",
    "TotalDPS": "total_dps",
    "TotalDot": "total_dot",
    "BleedDPS": "bleed_dps",
    "IgniteDPS": "ignite_dps",
    "IgniteDamage": "ignite_damage",
    "WithIgniteDPS": "total_dps_with_ignite",
    "WithIgniteAverageDamage": "average_damage_with_ignite",
    "PoisonDPS": "poison_dps",
    "PoisonDamage": "poison_damage",
    "WithPoisonDPS": "total_dps_with_poison",
    "WithPoisonAverageDamage": "average_damage_with_poison",
    "DecayDPS": "decay_dps",
    "Cooldown": "skill_cooldown",
    "AreaOfEffectRadius": "area_of_effect_radius",
    "ManaCost": "mana_cost",
    "Str": "strength",
    "ReqStr": "strength_required",
    "Dex": "dexterity",
    "ReqDex": "dexterity_required",
    "Int": "intelligence",
    "ReqInt": "intelligence_required",
    "Life": "life",
    "Spec:LifeInc": "life_increased",
    "LifeUnreserved": "life_unreserved",
    "LifeUnreservedPercent": "life_unreserved_percent",
    "LifeRegen": "life_regen",
    "LifeLeechGainRate": "life_leech_rate_per_hit",
    "LifeLeechGainPerHit": "life_leech_gain_per_hit",
    "Mana": "mana",
    "Spec:ManaInc": "mana_increased",
    "ManaUnreserved": "mana_unreserved",
    "ManaUnreservedPercent": "mana_unreserved_percent",
    "ManaRegen": "mana_regen",
    "ManaLeechGainRate": "mana_leech_rate_per_hit",
    "ManaLeechGainPerHit": "mana_leech_gain_per_hit",
    "TotalDegen": "total_degen",
    "NetRegen": "net_regen",
    "NetLifeRegen": "net_life_regen",
    "NetManaRegen": "net_mana_regen",
    "EnergyShield": "energy_shield",
    "Spec:EnergyShieldInc": "energy_shield_increased",
    "EnergyShieldRegen": "energy_shield_regen",
    "EnergyShieldLeechGainRate": "energy_shield_leech_rate_per_hit",
    "EnergyShieldLeechGainPerHit": "energy_shield_leech_gain_per_hit",
    "Evasion": "evasion",
    "Spec:EvasionInc": "evasion_increased",
    "MeleeEvadeChance": "melee_evade_chance",
    "ProjectileEvadeChance": "projectile_evade_chance",
    "Armour": "armour",
    "Spec:ArmourInc": "armour_increased",
    "PhysicalDamageReduction": "physical_damage_reduction",
    "EffectiveMovementSpeedMod": "effective_movement_speed_modifier",
    "BlockChance": "block_chance",
    "SpellBlockChance": "spell_block_chance",
    "AttackDodgeChance": "attack_dodge_chance",
    "SpellDodgeChance": "spell_dodge_chance",
    "FireResist": "fire_resistance",
    "ColdResist": "cold_resistance",
    "LightningResist": "lightning_resistance",
    "ChaosResist": "chaos_resistance",
    "FireResistOverCap": "fire_resistance_over_cap",
    "ColdResistOverCap": "cold_resistance_over_cap",
    "LightningResistOverCap": "lightning_resistance_over_cap",
    "ChaosResistOverCap": "chaos_resistance_over_cap",
    "PowerCharges": "power_charges",
    "PowerChargesMax": "power_charges_maximum",
    "FrenzyCharges": "frenzy_charges",
    "FrenzyChargesMax": "frenzy_charges_maximum",
    "EnduranceCharges": "endurance_charges",
    "EnduranceChargesMax": "endurance_charges_maximum",
    "ActiveTotemLimit": "active_totem_limit",
    "ActiveMinionLimit": "active_minion_limit"}
SET_MAP = {
    "Gloves": "gloves",
    "Weapon 1": "weapon1",
    "Flask 1": "flask1",
    "Belt Abyssal Socket 2": "belt_as2",
    "Flask 3": "flask3",
    "Body Armour Abyssal Socket 2": "body_armour_as2",
    "Amulet": "amulet",
    "Belt Abyssal Socket 1": "belt_as1",
    "Flask 2": "flask2",
    "Helmet Abyssal Socket 2": "helmet_as2",
    "Weapon 2": "weapon2",
    "Body Armour": "body_armour",
    "Belt": "belt",
    "Flask 5": "flask5",
    "Ring 2": "ring2",
    "Boots Abyssal Socket 2": "boots_as2",
    "Gloves Abyssal Socket 2": "gloves_as2",
    "Flask 4": "flask4",
    "Gloves Abyssal Socket 1": "gloves_as1",
    "Helmet Abyssal Socket 1": "helmet_as1",
    "Body Armour Abyssal Socket 1": "body_armour_as1",
    "Weapon 1 Swap": "weapon1_swap",
    "Boots": "boots",
    "Ring 1": "ring1",
    "Weapon 2 Swap": "weapon2_swap",
    "Helmet": "helmet",
    "Boots Abyssal Socket 1": "boots_as1",
    "Weapon 1 Abyssal Socket 1": "weapon1_as1",
    "Weapon 1 Abyssal Socket 2": "weapon1_as2",
    "Weapon 2 Abyssal Socket 1": "weapon2_as1",
    "Weapon 2 Abyssal Socket 2": "weapon2_as2",
    "Weapon 1Swap Abyssal Socket 1": "weapon1_swap_as1",
    "Weapon 1Swap Abyssal Socket 2": "weapon1_swap_as2",
    "Weapon 2Swap Abyssal Socket 1": "weapon2_swap_as1",
    "Weapon 2Swap Abyssal Socket 2": "weapon2_swap_as2"}
