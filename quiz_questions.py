#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📚 Mushroom Cultivation Quiz Questions Database

Comprehensive database of mushroom cultivation questions organized by
difficulty levels and topic categories for educational assessment.

File: quiz_questions.py
Author: Aaron J
Version: 2.0.0
Created: 2025-06-21
Last Modified: 2025-06-21

Description:
    This module contains the complete question database for the mushroom
    cultivation quiz application. It includes 111+ carefully crafted questions
    covering all aspects of mushroom cultivation, from basic biology to
    advanced growing techniques and medicinal properties.

Database Structure:
    Each question is a dictionary containing:
    - question: The question text
    - options: List of 4 multiple choice options
    - answer: The correct answer (must match one option exactly)
    - difficulty: "beginner", "intermediate", or "advanced"
    - explanation: Educational explanation of the correct answer
    - topic: Category for study recommendations

Statistics (as of v2.0.0):
    Total Questions: 111
    
    Difficulty Distribution:
    - Beginner: 38 questions (34.2%)
    - Intermediate: 46 questions (41.4%)
    - Advanced: 27 questions (24.3%)
    
    Topic Distribution:
    - Cultivation Process: 22 questions (19.8%)
    - Medicinal Mushrooms: 19 questions (17.1%)
    - Mushroom Varieties: 14 questions (12.6%)
    - Sterilization: 13 questions (11.7%)
    - Growing Conditions: 9 questions (8.1%)
    - Growing Methods: 8 questions (7.2%)
    - Biology Basics: 7 questions (6.3%)
    - Timing: 7 questions (6.3%)
    - Substrates: 6 questions (5.4%)
    - Beginner Varieties: 6 questions (5.4%)

Topics Covered:
    - Biology Basics: Fundamental fungal biology and terminology
    - Beginner Varieties: Entry-level mushroom species
    - Cultivation Process: Step-by-step growing procedures
    - Growing Conditions: Temperature, humidity, pH, CO2, lighting
    - Growing Methods: Different cultivation techniques and systems
    - Medicinal Mushrooms: Health benefits and active compounds
    - Mushroom Varieties: Species identification and characteristics
    - Sterilization: Contamination prevention and sterile techniques
    - Substrates: Growing media and nutrition
    - Timing: Schedules, harvest timing, and lifecycle stages

Functions:
    get_questions_by_difficulty(difficulty): Filter questions by difficulty
    get_questions_count(): Get total number of questions
    get_difficulty_distribution(): Get question counts by difficulty
    get_topic_distribution(): Get question counts by topic

Usage:
    from quiz_questions import get_questions_by_difficulty, QUESTIONS
    beginner_questions = get_questions_by_difficulty("beginner")
    all_questions = QUESTIONS

Data Quality:
    - All questions thoroughly researched and fact-checked
    - Explanations provide educational value beyond just answers
    - Balanced coverage across all cultivation aspects
    - Progressive difficulty appropriate for skill levels
    - Real-world applicable knowledge

Maintenance:
    - Questions can be easily added to the QUESTIONS list
    - Follow existing format for consistency
    - Ensure all topics and difficulties are represented
    - Verify answer accuracy and explanation quality

License:
    MIT License - See LICENSE file for details
"""

# Comprehensive Questions Database
QUESTIONS = [
    {
        "question": "What is the optimal temperature range for growing most gourmet mushrooms?",
        "options": ["15-20°C (59-68°F)", "20-25°C (68-77°F)", "25-30°C (77-86°F)", "10-15°C (50-59°F)"],
        "answer": "20-25°C (68-77°F)",
        "difficulty": "beginner",
        "explanation": "Most gourmet mushrooms like oyster, shiitake, and lion's mane thrive in the 20-25°C range.",
        "topic": "growing_conditions"
    },
    {
        "question": "What is the scientific name for the common button mushroom?",
        "options": ["Pleurotus ostreatus", "Agaricus bisporus", "Lentinula edodes", "Hericium erinaceus"],
        "answer": "Agaricus bisporus",
        "difficulty": "intermediate",
        "explanation": "Agaricus bisporus includes white button, cremini, and portobello mushrooms - all the same species at different stages!",
        "topic": "mushroom_varieties"
    },
    {
        "question": "Which substrate is most commonly used for growing oyster mushrooms?",
        "options": ["Hardwood sawdust", "Coffee grounds", "Wheat straw", "All of the above"],
        "answer": "All of the above",
        "difficulty": "beginner",
        "explanation": "Oyster mushrooms are very adaptable and can grow on various organic substrates!",
        "topic": "substrates"
    },
    {
        "question": "What is mycelium?",
        "options": ["The fruiting body of mushrooms", "The vegetative network of fungal threads", "A mushroom disease", "A type of spore"],
        "answer": "The vegetative network of fungal threads",
        "difficulty": "beginner",
        "explanation": "Mycelium is like the 'root system' of fungi, made up of tiny threads called hyphae.",
        "topic": "biology_basics"
    },
    {
        "question": "What is the most effective method for sterilizing mushroom substrate?",
        "options": ["Boiling water", "Pressure cooking/steaming", "Microwave heating", "Solar drying"],
        "answer": "Pressure cooking/steaming",
        "difficulty": "intermediate",
        "explanation": "Pressure cooking at 15 PSI for 60-90 minutes effectively kills competing microorganisms.",
        "topic": "sterilization"
    },
    {
        "question": "What humidity level is typically needed for mushroom fruiting?",
        "options": ["40-60%", "60-80%", "80-95%", "95-100%"],
        "answer": "80-95%",
        "difficulty": "intermediate",
        "explanation": "High humidity prevents mushrooms from drying out during development.",
        "topic": "growing_conditions"
    },
    {
        "question": "Which mushroom is known as the 'King of Medicinal Mushrooms'?",
        "options": ["Shiitake", "Reishi (Ganoderma lucidum)", "Turkey Tail", "Cordyceps"],
        "answer": "Reishi (Ganoderma lucidum)",
        "difficulty": "advanced",
        "explanation": "Reishi has been used in traditional medicine for over 2000 years!",
        "topic": "medicinal_mushrooms"
    },
    {
        "question": "What does 'inoculation' mean in mushroom cultivation?",
        "options": ["Harvesting mushrooms", "Adding spores/spawn to substrate", "Watering the mushrooms", "Creating fruiting conditions"],
        "answer": "Adding spores/spawn to substrate",
        "difficulty": "beginner",
        "explanation": "Inoculation is introducing the mushroom culture to the growing medium.",
        "topic": "cultivation_process"
    },
    {
        "question": "Which mushroom is easiest for beginners to grow?",
        "options": ["Shiitake", "Lion's Mane", "Oyster mushrooms", "Morel mushrooms"],
        "answer": "Oyster mushrooms",
        "difficulty": "beginner",
        "explanation": "Oyster mushrooms are forgiving, fast-growing, and can handle various conditions.",
        "topic": "beginner_varieties"
    },
    {
        "question": "What is 'pinning' in mushroom cultivation?",
        "options": ["Harvesting technique", "Initial formation of mushroom primordia", "Substrate preparation", "Pest control method"],
        "answer": "Initial formation of mushroom primordia",
        "difficulty": "intermediate",
        "explanation": "Pins are tiny mushroom buds that form before developing into full mushrooms.",
        "topic": "cultivation_process"
    },
    {
        "question": "Which growing method uses logs as substrate?",
        "options": ["Bag cultivation", "Tray cultivation", "Log cultivation", "Bottle cultivation"],
        "answer": "Log cultivation",
        "difficulty": "beginner",
        "explanation": "Log cultivation mimics how mushrooms grow naturally in the forest.",
        "topic": "growing_methods"
    },
    {
        "question": "What is the typical pH range for mushroom substrate?",
        "options": ["4.0-5.5", "5.5-7.0", "7.0-8.5", "8.5-10.0"],
        "answer": "5.5-7.0",
        "difficulty": "advanced",
        "explanation": "Most mushrooms prefer slightly acidic to neutral conditions.",
        "topic": "growing_conditions"
    },
    {
        "question": "How long does it typically take for oyster mushrooms to fruit after inoculation?",
        "options": ["1-2 weeks", "2-4 weeks", "4-6 weeks", "6-8 weeks"],
        "answer": "2-4 weeks",
        "difficulty": "intermediate",
        "explanation": "Oyster mushrooms are among the fastest-fruiting gourmet varieties.",
        "topic": "timing"
    },
    {
        "question": "What is 'spawn' in mushroom cultivation?",
        "options": ["Baby mushrooms", "Mushroom spores", "Mycelium grown on grain or other substrate", "Harvested mushrooms"],
        "answer": "Mycelium grown on grain or other substrate",
        "difficulty": "beginner",
        "explanation": "Spawn is like 'mushroom seeds' - viable mycelium ready to inoculate new substrate.",
        "topic": "cultivation_process"
    },
    {
        "question": "Which mushroom variety can be grown on coffee grounds?",
        "options": ["Shiitake only", "Oyster mushrooms only", "Button mushrooms only", "Multiple varieties including oyster and shiitake"],
        "answer": "Multiple varieties including oyster and shiitake",
        "difficulty": "intermediate",
        "explanation": "Used coffee grounds are an excellent, often free substrate for many mushroom varieties!",
        "topic": "substrates"
    },
    {
        "question": "What is the scientific name for Shiitake mushrooms?",
        "options": ["Lentinula edodes", "Pleurotus ostreatus", "Agaricus bisporus", "Hericium erinaceus"],
        "answer": "Lentinula edodes",
        "difficulty": "intermediate",
        "explanation": "Shiitake (Lentinula edodes) is one of the most popular gourmet mushrooms worldwide.",
        "topic": "mushroom_varieties"
    },
    {
        "question": "What does 'pasteurization' accomplish in mushroom cultivation?",
        "options": ["Kills all microorganisms", "Reduces competing bacteria while preserving beneficial microbes", "Adds nutrients to substrate", "Increases moisture content"],
        "answer": "Reduces competing bacteria while preserving beneficial microbes",
        "difficulty": "intermediate",
        "explanation": "Pasteurization is gentler than sterilization and maintains some beneficial microorganisms.",
        "topic": "sterilization"
    },
    {
        "question": "Which mushroom is known for its brain-like appearance?",
        "options": ["Lion's Mane", "Cauliflower Mushroom", "Coral Mushroom", "Chicken of the Woods"],
        "answer": "Lion's Mane",
        "difficulty": "beginner",
        "explanation": "Lion's Mane (Hericium erinaceus) has distinctive white, shaggy spines resembling a lion's mane.",
        "topic": "mushroom_varieties"
    },
    {
        "question": "What is the ideal CO2 level during mushroom fruiting?",
        "options": ["Very high (5000+ ppm)", "High (1000-3000 ppm)", "Low (400-800 ppm)", "Zero CO2"],
        "answer": "Low (400-800 ppm)",
        "difficulty": "advanced",
        "explanation": "During fruiting, mushrooms need fresh air with low CO2 to develop properly.",
        "topic": "growing_conditions"
    },
    {
        "question": "What is 'flushing' in mushroom cultivation?",
        "options": ["Cleaning the growing area", "Waves of mushroom production", "Removing old substrate", "Adding water to substrate"],
        "answer": "Waves of mushroom production",
        "difficulty": "intermediate",
        "explanation": "Mushrooms typically grow in multiple flushes or waves from the same substrate.",
        "topic": "cultivation_process"
    },
    {
        "question": "Which substrate is traditionally used for growing Shiitake?",
        "options": ["Straw", "Hardwood logs or sawdust", "Corn cobs", "Coconut coir"],
        "answer": "Hardwood logs or sawdust",
        "difficulty": "beginner",
        "explanation": "Shiitake naturally grows on hardwood trees and thrives on oak, maple, and other hardwood substrates.",
        "topic": "substrates"
    },
    {
        "question": "What is the main purpose of the incubation period?",
        "options": ["Mushroom formation", "Mycelium colonization of substrate", "Harvesting preparation", "Pest prevention"],
        "answer": "Mycelium colonization of substrate",
        "difficulty": "beginner",
        "explanation": "During incubation, mycelium spreads throughout the substrate before fruiting begins.",
        "topic": "cultivation_process"
    },
    {
        "question": "Which mushroom is known for its oyster shell-like shape?",
        "options": ["Button mushroom", "Oyster mushroom", "Shiitake", "Enoki"],
        "answer": "Oyster mushroom",
        "difficulty": "beginner",
        "explanation": "Oyster mushrooms (Pleurotus species) have a distinctive fan or oyster shell shape.",
        "topic": "mushroom_varieties"
    },
    {
        "question": "What is 'autoclave' sterilization?",
        "options": ["Steam sterilization under pressure", "Chemical sterilization", "UV light sterilization", "Heat-only sterilization"],
        "answer": "Steam sterilization under pressure",
        "difficulty": "intermediate",
        "explanation": "Autoclaves use pressurized steam at 121°C to achieve complete sterilization.",
        "topic": "sterilization"
    },
    {
        "question": "Which mushroom has extremely long, thin white stems?",
        "options": ["Enoki", "Maitake", "Shiitake", "Cremini"],
        "answer": "Enoki",
        "difficulty": "beginner",
        "explanation": "Enoki mushrooms are characterized by their long, thin white stems and tiny caps.",
        "topic": "mushroom_varieties"
    },
    {
        "question": "What causes mushrooms to develop tough, rubbery texture?",
        "options": ["Too much water", "High temperature", "Low humidity", "Excessive CO2"],
        "answer": "Low humidity",
        "difficulty": "intermediate",
        "explanation": "Low humidity causes mushrooms to dry out and become tough during development.",
        "topic": "growing_conditions"
    },
    {
        "question": "Which growing technique involves drilling holes in logs?",
        "options": ["Bag cultivation", "Tray cultivation", "Log inoculation", "Bottle cultivation"],
        "answer": "Log inoculation",
        "difficulty": "beginner",
        "explanation": "In log cultivation, holes are drilled and filled with spawn, then sealed with wax.",
        "topic": "growing_methods"
    },
    {
        "question": "What is 'contamination' in mushroom cultivation?",
        "options": ["Mushroom disease", "Unwanted microorganisms competing with mushrooms", "Substrate spoilage", "Poor mushroom quality"],
        "answer": "Unwanted microorganisms competing with mushrooms",
        "difficulty": "beginner",
        "explanation": "Contamination refers to bacteria, molds, or other fungi that compete with desired mushrooms.",
        "topic": "cultivation_process"
    },
    {
        "question": "Which mushroom is also called 'Hen of the Woods'?",
        "options": ["Maitake", "Chicken of the Woods", "Turkey Tail", "Lion's Mane"],
        "answer": "Maitake",
        "difficulty": "intermediate",
        "explanation": "Maitake (Grifola frondosa) is also known as Hen of the Woods due to its clustered appearance.",
        "topic": "mushroom_varieties"
    },
    {
        "question": "What is the optimal moisture content for most mushroom substrates?",
        "options": ["40-50%", "60-70%", "80-90%", "95-100%"],
        "answer": "60-70%",
        "difficulty": "advanced",
        "explanation": "Most substrates should have 60-70% moisture content for optimal mushroom growth.",
        "topic": "growing_conditions"
    },
    {
        "question": "Which mushroom can be found growing on dead or dying trees?",
        "options": ["All of the above", "Oyster mushrooms", "Shiitake", "Chicken of the Woods"],
        "answer": "All of the above",
        "difficulty": "beginner",
        "explanation": "Many mushrooms are saprophytic, meaning they grow on dead or decaying wood.",
        "topic": "biology_basics"
    },
    {
        "question": "What does 'agar' refer to in mushroom cultivation?",
        "options": ["A type of mushroom", "Growth medium for tissue culture", "Substrate additive", "Sterilization chemical"],
        "answer": "Growth medium for tissue culture",
        "difficulty": "advanced",
        "explanation": "Agar is a gel-like substance used to grow mushroom cultures in laboratory conditions.",
        "topic": "cultivation_process"
    },
    {
        "question": "Which factor is most important for preventing contamination?",
        "options": ["Temperature control", "Cleanliness and sterile technique", "Proper lighting", "Substrate type"],
        "answer": "Cleanliness and sterile technique",
        "difficulty": "intermediate",
        "explanation": "Maintaining sterile conditions is crucial to prevent unwanted microorganisms.",
        "topic": "sterilization"
    },
    {
        "question": "What is 'liquid culture' in mushroom cultivation?",
        "options": ["Watering system", "Mycelium grown in nutrient liquid", "Liquid fertilizer", "Sterilization solution"],
        "answer": "Mycelium grown in nutrient liquid",
        "difficulty": "advanced",
        "explanation": "Liquid culture allows rapid multiplication of mycelium in a sterile nutrient solution.",
        "topic": "cultivation_process"
    },
    {
        "question": "Which mushroom variety is known for its medicinal beta-glucan content?",
        "options": ["All gourmet mushrooms", "Only Reishi", "Only Shiitake", "Only Turkey Tail"],
        "answer": "All gourmet mushrooms",
        "difficulty": "intermediate",
        "explanation": "Most gourmet mushrooms contain beneficial beta-glucans, though concentrations vary.",
        "topic": "medicinal_mushrooms"
    },
    {
        "question": "What is 'tissue culture' in mushroom cultivation?",
        "options": ["Growing mushrooms from tissue samples", "Harvesting mushroom tissue", "Storing mushroom samples", "Testing mushroom quality"],
        "answer": "Growing mushrooms from tissue samples",
        "difficulty": "advanced",
        "explanation": "Tissue culture involves growing mushrooms from small pieces of mushroom tissue on sterile media.",
        "topic": "cultivation_process"
    },
    {
        "question": "Which mushroom is orange/yellow and grows in clusters on wood?",
        "options": ["Chicken of the Woods", "Chanterelle", "Golden Oyster", "Honey Mushroom"],
        "answer": "Chicken of the Woods",
        "difficulty": "beginner",
        "explanation": "Chicken of the Woods (Laetiporus species) forms bright orange/yellow bracket-like clusters.",
        "topic": "mushroom_varieties"
    },
    {
        "question": "What happens during the 'pinning' trigger?",
        "options": ["Temperature drop and fresh air introduction", "Increased humidity only", "Addition of nutrients", "Substrate replacement"],
        "answer": "Temperature drop and fresh air introduction",
        "difficulty": "intermediate",
        "explanation": "Pinning is typically triggered by environmental changes like temperature drop and fresh air.",
        "topic": "cultivation_process"
    },
    {
        "question": "Which substrate additive helps maintain proper pH?",
        "options": ["Lime (calcium carbonate)", "Salt", "Sugar", "Vinegar"],
        "answer": "Lime (calcium carbonate)",
        "difficulty": "advanced",
        "explanation": "Lime helps buffer substrate pH and provides calcium for mushroom development.",
        "topic": "substrates"
    },
    {
        "question": "What is the typical harvest time for most gourmet mushrooms?",
        "options": ["When caps are fully opened", "Just before or as caps begin to flatten", "When spores are released", "After caps turn dark"],
        "answer": "Just before or as caps begin to flatten",
        "difficulty": "intermediate",
        "explanation": "Mushrooms are best harvested when caps are still slightly curved for optimal texture and flavor.",
        "topic": "timing"
    },
    {
        "question": "Which mushroom is known for growing in a tree-like cluster formation?",
        "options": ["Maitake", "Enoki", "Button mushrooms", "Lion's Mane"],
        "answer": "Maitake",
        "difficulty": "beginner",
        "explanation": "Maitake grows in distinctive overlapping, tree-like clusters from a central base.",
        "topic": "mushroom_varieties"
    },
    {
        "question": "What is 'sterile technique'?",
        "options": ["Working in completely sterile conditions", "Using only sterilized tools and maintaining cleanliness", "Avoiding all contact with substrate", "Working only at night"],
        "answer": "Using only sterilized tools and maintaining cleanliness",
        "difficulty": "intermediate",
        "explanation": "Sterile technique involves using sterilized tools and maintaining clean conditions to prevent contamination.",
        "topic": "sterilization"
    },
    {
        "question": "Which environmental factor triggers mushroom formation?",
        "options": ["Fresh air exchange", "Light exposure", "Temperature changes", "All of the above"],
        "answer": "All of the above",
        "difficulty": "intermediate",
        "explanation": "Mushroom formation is triggered by multiple environmental factors working together.",
        "topic": "growing_conditions"
    },
    {
        "question": "Which gourmet mushroom is known for its crab-like flavor and is often used as a seafood substitute?",
        "options": ["King Oyster", "Lion's Mane", "Blue Oyster", "Phoenix Oyster"],
        "answer": "Lion's Mane",
        "difficulty": "intermediate",
        "explanation": "Lion's Mane has a unique texture and seafood-like flavor, making it popular as a crab or lobster substitute in vegan dishes.",
        "topic": "mushroom_varieties"
    },
    {
        "question": "What is the optimal substrate for King Oyster mushrooms (Pleurotus eryngii)?",
        "options": ["Pure straw", "Hardwood sawdust with bran supplement", "Coffee grounds only", "Coconut coir"],
        "answer": "Hardwood sawdust with bran supplement",
        "difficulty": "intermediate",
        "explanation": "King Oysters prefer hardwood sawdust supplemented with wheat bran or other nitrogen sources for optimal growth.",
        "topic": "substrates"
    },
    {
        "question": "Which gourmet mushroom requires the coldest fruiting temperature?",
        "options": ["Shiitake", "Oyster mushrooms", "Enoki", "Lion's Mane"],
        "answer": "Enoki",
        "difficulty": "advanced",
        "explanation": "Enoki mushrooms fruit best at 10-13°C (50-55°F), much cooler than most other gourmet varieties.",
        "topic": "growing_conditions"
    },
    {
        "question": "What is the scientific name for King Oyster mushrooms?",
        "options": ["Pleurotus ostreatus", "Pleurotus eryngii", "Pleurotus citrinopileatus", "Pleurotus pulmonarius"],
        "answer": "Pleurotus eryngii",
        "difficulty": "advanced",
        "explanation": "Pleurotus eryngii, the King Oyster, is the largest of the oyster mushroom species with thick, meaty stems.",
        "topic": "mushroom_varieties"
    },
    {
        "question": "Which gourmet mushroom is known for its wine-red color when fresh?",
        "options": ["Red Reishi", "Wine Cap Stropharia", "Elm Oyster", "Shiitake"],
        "answer": "Wine Cap Stropharia",
        "difficulty": "intermediate",
        "explanation": "Wine Cap Stropharia (Stropharia rugosoannulata) has a distinctive wine-red cap when young and fresh.",
        "topic": "mushroom_varieties"
    },
    {
        "question": "What makes Pink Oyster mushrooms (Pleurotus djamor) unique among oyster varieties?",
        "options": ["They grow only on hardwood", "They require higher temperatures than other oysters", "They are the smallest oyster variety", "They only fruit in winter"],
        "answer": "They require higher temperatures than other oysters",
        "difficulty": "intermediate",
        "explanation": "Pink Oysters are tropical and require warmer temperatures (25-30°C) compared to other oyster mushroom varieties.",
        "topic": "growing_conditions"
    },
    {
        "question": "Which mushroom is known as the 'Beefsteak Mushroom' due to its meat-like appearance?",
        "options": ["King Oyster", "Lion's Mane", "Beefsteak Polypore", "Maitake"],
        "answer": "Beefsteak Polypore",
        "difficulty": "beginner",
        "explanation": "The Beefsteak Polypore (Fistulina hepatica) resembles raw beef with its red, juicy appearance.",
        "topic": "mushroom_varieties"
    },
    {
        "question": "What is the most challenging aspect of cultivating morel mushrooms commercially?",
        "options": ["High temperature requirements", "Complex life cycle requiring specific soil conditions", "Very slow growth rate", "Excessive moisture needs"],
        "answer": "Complex life cycle requiring specific soil conditions",
        "difficulty": "advanced",
        "explanation": "Morels have a complex life cycle and specific soil microbiome requirements that make commercial cultivation extremely difficult.",
        "topic": "cultivation_process"
    },
    {
        "question": "Which gourmet mushroom is best known for its anti-aging and longevity properties?",
        "options": ["Shiitake", "Reishi", "Cordyceps", "Turkey Tail"],
        "answer": "Reishi",
        "difficulty": "intermediate",
        "explanation": "Reishi (Ganoderma lucidum) has been called the 'mushroom of immortality' in traditional Chinese medicine for its longevity benefits.",
        "topic": "medicinal_mushrooms"
    },
    {
        "question": "What distinguishes Elm Oyster mushrooms from regular oyster mushrooms?",
        "options": ["They grow only on elm trees", "They have a longer shelf life and firmer texture", "They are much smaller", "They require colder temperatures"],
        "answer": "They have a longer shelf life and firmer texture",
        "difficulty": "intermediate",
        "explanation": "Elm Oysters (Hypsizygus ulmarius) have a firmer texture and better shelf life than common oyster mushrooms.",
        "topic": "mushroom_varieties"
    },
    {
        "question": "Which substrate supplement is commonly added to increase protein content for gourmet mushrooms?",
        "options": ["Sand", "Soybean meal or wheat bran", "Perlite", "Activated charcoal"],
        "answer": "Soybean meal or wheat bran",
        "difficulty": "advanced",
        "explanation": "Protein-rich supplements like soybean meal and wheat bran boost mushroom yields and nutritional content.",
        "topic": "substrates"
    },
    {
        "question": "What is the typical growing cycle time for Shiitake mushrooms from inoculation to harvest?",
        "options": ["2-4 weeks", "6-12 weeks", "3-6 months", "1-2 years"],
        "answer": "6-12 weeks",
        "difficulty": "intermediate",
        "explanation": "Shiitake takes longer than oyster mushrooms, typically requiring 6-12 weeks for full colonization and fruiting.",
        "topic": "timing"
    },
    {
        "question": "Which mushroom variety is known for producing natural vitamin D when exposed to UV light?",
        "options": ["Only Shiitake", "Only Maitake", "All mushrooms can produce vitamin D", "Only white button mushrooms"],
        "answer": "All mushrooms can produce vitamin D",
        "difficulty": "advanced",
        "explanation": "Most mushrooms can convert ergosterol to vitamin D2 when exposed to UV light, making them excellent vitamin D sources.",
        "topic": "medicinal_mushrooms"
    },
    {
        "question": "What makes Blue Oyster mushrooms blue?",
        "options": ["Special growing conditions", "Natural pigments in the mushroom", "Cold temperature exposure", "UV light exposure"],
        "answer": "Natural pigments in the mushroom",
        "difficulty": "beginner",
        "explanation": "Blue Oysters (Pleurotus columbinus) contain natural blue pigments that give them their distinctive color.",
        "topic": "mushroom_varieties"
    },
    {
        "question": "Which growing technique allows for the highest yield per square foot for gourmet mushrooms?",
        "options": ["Log cultivation", "Vertical growing systems", "Traditional tray method", "Ground bed cultivation"],
        "answer": "Vertical growing systems",
        "difficulty": "intermediate",
        "explanation": "Vertical growing systems maximize space utilization by stacking growing containers, achieving higher yields per square foot.",
        "topic": "growing_methods"
    },
    {
        "question": "What are hyphae?",
        "options": ["Mushroom spores", "Thread-like structures that make up mycelium", "Mushroom caps", "Root systems"],
        "answer": "Thread-like structures that make up mycelium",
        "difficulty": "beginner",
        "explanation": "Hyphae are the basic building blocks of fungal mycelium - tiny thread-like structures that grow and branch.",
        "topic": "biology_basics"
    },
    {
        "question": "What is the difference between saprophytic and parasitic fungi?",
        "options": ["Saprophytic fungi eat dead matter, parasitic fungi attack living organisms", "No difference", "Saprophytic fungi are bigger", "Parasitic fungi only grow in water"],
        "answer": "Saprophytic fungi eat dead matter, parasitic fungi attack living organisms",
        "difficulty": "intermediate",
        "explanation": "Most cultivated mushrooms are saprophytic, decomposing dead organic matter rather than harming living plants.",
        "topic": "biology_basics"
    },
    {
        "question": "What is a mushroom's reproductive purpose?",
        "options": ["To feed the mycelium", "To produce and spread spores", "To store nutrients", "To attract insects"],
        "answer": "To produce and spread spores",
        "difficulty": "beginner",
        "explanation": "Mushrooms are the fruiting bodies that produce and release spores for reproduction.",
        "topic": "biology_basics"
    },
    {
        "question": "What are spores in mushroom biology?",
        "options": ["Baby mushrooms", "Fungal seeds for reproduction", "Mushroom food", "Disease particles"],
        "answer": "Fungal seeds for reproduction",
        "difficulty": "beginner",
        "explanation": "Spores are like seeds - they allow fungi to reproduce and colonize new areas.",
        "topic": "biology_basics"
    },
    {
        "question": "Why do fungi not have chlorophyll?",
        "options": ["They don't need sunlight because they decompose organic matter", "They are too small", "They live underground", "They get chlorophyll from plants"],
        "answer": "They don't need sunlight because they decompose organic matter",
        "difficulty": "intermediate",
        "explanation": "Unlike plants, fungi get energy by breaking down organic matter rather than photosynthesis.",
        "topic": "biology_basics"
    },
    {
        "question": "Which mushroom variety is recommended as the absolute best for first-time growers?",
        "options": ["Shiitake", "Oyster mushrooms", "Lion's Mane", "Enoki"],
        "answer": "Oyster mushrooms",
        "difficulty": "beginner",
        "explanation": "Oyster mushrooms are forgiving, fast-growing, and can handle temperature and humidity fluctuations.",
        "topic": "beginner_varieties"
    },
    {
        "question": "What makes oyster mushrooms ideal for beginners?",
        "options": ["They grow very slowly", "They are tolerant of varying conditions", "They need special equipment", "They only grow in winter"],
        "answer": "They are tolerant of varying conditions",
        "difficulty": "beginner",
        "explanation": "Oyster mushrooms can tolerate temperature and humidity variations that would harm other varieties.",
        "topic": "beginner_varieties"
    },
    {
        "question": "Which beginner-friendly mushroom can grow at room temperature?",
        "options": ["Enoki", "Shiitake", "Oyster mushrooms", "Morels"],
        "answer": "Oyster mushrooms",
        "difficulty": "beginner",
        "explanation": "Many oyster mushroom varieties can fruit successfully at normal room temperatures (18-24°C).",
        "topic": "beginner_varieties"
    },
    {
        "question": "What is the easiest substrate for a beginner to start with?",
        "options": ["Sterilized hardwood sawdust", "Used coffee grounds", "Fresh straw", "Garden soil"],
        "answer": "Used coffee grounds",
        "difficulty": "beginner",
        "explanation": "Coffee grounds are pre-pasteurized, often free, and work well for oyster mushrooms.",
        "topic": "beginner_varieties"
    },
    {
        "question": "Which oyster mushroom variety is most tolerant for beginners?",
        "options": ["King Oyster", "Pink Oyster", "Blue Oyster", "Phoenix Oyster"],
        "answer": "Phoenix Oyster",
        "difficulty": "beginner",
        "explanation": "Phoenix Oyster (Pleurotus pulmonarius) is extremely hardy and forgiving of beginner mistakes.",
        "topic": "beginner_varieties"
    },
    {
        "question": "How long should you wait between harvesting flushes?",
        "options": ["1-3 days", "1-2 weeks", "1 month", "3 months"],
        "answer": "1-2 weeks",
        "difficulty": "intermediate",
        "explanation": "Most substrates need 1-2 weeks of rest between flushes to rebuild energy for the next harvest.",
        "topic": "timing"
    },
    {
        "question": "What time of day is best for harvesting mushrooms?",
        "options": ["Early morning", "Midday", "Evening", "Time doesn't matter"],
        "answer": "Early morning",
        "difficulty": "intermediate",
        "explanation": "Early morning harvesting captures mushrooms at peak freshness before they release spores.",
        "topic": "timing"
    },
    {
        "question": "How quickly should harvested mushrooms be used or preserved?",
        "options": ["Within 1-2 hours", "Within 3-7 days", "Within 2 weeks", "Within 1 month"],
        "answer": "Within 3-7 days",
        "difficulty": "beginner",
        "explanation": "Fresh mushrooms should be used within a week when refrigerated, or preserved by drying or freezing.",
        "topic": "timing"
    },
    {
        "question": "How long can mushroom spawn be stored before use?",
        "options": ["1-2 days", "1-2 weeks", "2-6 months when refrigerated", "Several years"],
        "answer": "2-6 months when refrigerated",
        "difficulty": "intermediate",
        "explanation": "Properly stored spawn can remain viable for months in the refrigerator, but fresher is always better.",
        "topic": "timing"
    },
    {
        "question": "What is 'monotub' cultivation?",
        "options": ["Growing one mushroom at a time", "Large plastic container growing system", "Growing in tubes", "Single flush method"],
        "answer": "Large plastic container growing system",
        "difficulty": "intermediate",
        "explanation": "Monotub is a popular method using large plastic storage containers with air holes for growing mushrooms.",
        "topic": "growing_methods"
    },
    {
        "question": "What is 'shotgun fruiting chamber' (SGFC)?",
        "options": ["Rapid harvesting technique", "Container with many small holes for air exchange", "High-pressure growing system", "Automated watering system"],
        "answer": "Container with many small holes for air exchange",
        "difficulty": "intermediate",
        "explanation": "SGFC uses hundreds of small holes to create passive air exchange for mushroom fruiting.",
        "topic": "growing_methods"
    },
    {
        "question": "What is 'bulk substrate' growing?",
        "options": ["Growing large mushrooms", "Using large quantities of mixed substrate materials", "Commercial growing only", "Growing in bulk containers"],
        "answer": "Using large quantities of mixed substrate materials",
        "difficulty": "advanced",
        "explanation": "Bulk substrate involves mixing spawn with large amounts of nutritious substrate for higher yields.",
        "topic": "growing_methods"
    },
    {
        "question": "What advantage does bag cultivation have over other methods?",
        "options": ["Higher yields", "Better contamination control and portability", "Faster growth", "Lower cost"],
        "answer": "Better contamination control and portability",
        "difficulty": "intermediate",
        "explanation": "Growing bags provide contained environments that reduce contamination risk and are easy to move.",
        "topic": "growing_methods"
    },
    {
        "question": "What is 'martha tent' cultivation?",
        "options": ["Outdoor growing method", "High-humidity tent system for mushroom growing", "Winter growing technique", "Sterilization method"],
        "answer": "High-humidity tent system for mushroom growing",
        "difficulty": "advanced",
        "explanation": "Martha tents use plastic sheeting and humidifiers to create controlled high-humidity environments.",
        "topic": "growing_methods"
    },
    {
        "question": "What temperature should substrate reach during steam sterilization?",
        "options": ["80°C (176°F)", "100°C (212°F)", "121°C (250°F)", "150°C (302°F)"],
        "answer": "121°C (250°F)",
        "difficulty": "intermediate",
        "explanation": "Steam sterilization requires 121°C at 15 PSI to effectively kill all microorganisms including spores.",
        "topic": "sterilization"
    },
    {
        "question": "How long should substrate be sterilized in a pressure cooker?",
        "options": ["15-30 minutes", "60-90 minutes", "2-3 hours", "24 hours"],
        "answer": "60-90 minutes",
        "difficulty": "beginner",
        "explanation": "Most substrates need 60-90 minutes at 15 PSI to ensure complete sterilization.",
        "topic": "sterilization"
    },
    {
        "question": "What is the difference between sterilization and pasteurization?",
        "options": ["No difference", "Sterilization kills everything, pasteurization reduces harmful microbes", "Pasteurization is hotter", "Sterilization uses chemicals"],
        "answer": "Sterilization kills everything, pasteurization reduces harmful microbes",
        "difficulty": "intermediate",
        "explanation": "Sterilization eliminates all life, while pasteurization reduces pathogens but preserves some beneficial microbes.",
        "topic": "sterilization"
    },
    {
        "question": "Which sterilization method is best for heat-sensitive materials?",
        "options": ["Pressure cooking", "Boiling water", "Chemical sterilization", "Dry heat"],
        "answer": "Chemical sterilization",
        "difficulty": "advanced",
        "explanation": "Chemical sterilants like hydrogen peroxide or alcohol can sterilize without high heat damage.",
        "topic": "sterilization"
    },
    {
        "question": "What should you do with tools before using them in mushroom cultivation?",
        "options": ["Just rinse with water", "Wipe with a cloth", "Sterilize with alcohol or flame", "Nothing special needed"],
        "answer": "Sterilize with alcohol or flame",
        "difficulty": "beginner",
        "explanation": "All tools should be sterilized to prevent introducing contaminants to your mushroom culture.",
        "topic": "sterilization"
    },
    {
        "question": "Why is a laminar flow hood used in mushroom cultivation?",
        "options": ["To increase humidity", "To provide sterile air flow", "To heat the substrate", "To add CO2"],
        "answer": "To provide sterile air flow",
        "difficulty": "advanced",
        "explanation": "Laminar flow hoods create a sterile workspace by filtering air and directing it in a uniform flow.",
        "topic": "sterilization"
    },
    {
        "question": "What concentration of isopropyl alcohol is most effective for sterilization?",
        "options": ["50%", "70%", "90%", "100%"],
        "answer": "70%",
        "difficulty": "intermediate",
        "explanation": "70% alcohol is more effective than higher concentrations because water helps the alcohol penetrate cell walls.",
        "topic": "sterilization"
    },
    {
        "question": "How can you test if your sterilization process is working?",
        "options": ["Check temperature only", "Use biological indicators or spore strips", "Visual inspection", "Smell test"],
        "answer": "Use biological indicators or spore strips",
        "difficulty": "advanced",
        "explanation": "Biological indicators contain heat-resistant spores that confirm sterilization was effective.",
        "topic": "sterilization"
    },
    {
        "question": "What is the first step in the mushroom cultivation process?",
        "options": ["Harvesting", "Inoculation", "Substrate preparation", "Creating fruiting conditions"],
        "answer": "Substrate preparation",
        "difficulty": "beginner",
        "explanation": "You must first prepare and sterilize the growing medium before adding mushroom spawn.",
        "topic": "cultivation_process"
    },
    {
        "question": "What happens during the colonization phase?",
        "options": ["Mushrooms form", "Mycelium spreads through substrate", "Spores are released", "Harvesting occurs"],
        "answer": "Mycelium spreads through substrate",
        "difficulty": "beginner",
        "explanation": "During colonization, the mycelium grows throughout the substrate before mushroom formation begins.",
        "topic": "cultivation_process"
    },
    {
        "question": "What environmental change typically triggers the transition from colonization to fruiting?",
        "options": ["Increased temperature", "Decreased humidity", "Fresh air exchange and light", "Adding nutrients"],
        "answer": "Fresh air exchange and light",
        "difficulty": "intermediate",
        "explanation": "The transition to fruiting is triggered by environmental changes that signal it's time to reproduce.",
        "topic": "cultivation_process"
    },
    {
        "question": "What is 'spawn run' in mushroom cultivation?",
        "options": ["Harvesting period", "Initial colonization period", "Mushroom growth phase", "Sterilization process"],
        "answer": "Initial colonization period",
        "difficulty": "intermediate",
        "explanation": "Spawn run is the period when mycelium from spawn spreads through and colonizes the substrate.",
        "topic": "cultivation_process"
    },
    {
        "question": "How do you know when substrate is fully colonized?",
        "options": ["It turns black", "White mycelium covers the entire surface", "It starts smelling bad", "It becomes hard"],
        "answer": "White mycelium covers the entire surface",
        "difficulty": "beginner",
        "explanation": "Full colonization is indicated by white, fluffy mycelium covering the entire substrate surface.",
        "topic": "cultivation_process"
    },
    {
        "question": "What is 'casing' in mushroom cultivation?",
        "options": ["Packaging mushrooms", "Adding a top layer of non-nutritive material", "Sterilization method", "Harvesting technique"],
        "answer": "Adding a top layer of non-nutritive material",
        "difficulty": "advanced",
        "explanation": "Casing involves adding a layer of material like peat moss to help trigger and support mushroom formation.",
        "topic": "cultivation_process"
    },
    {
        "question": "What should you do if you see green or black mold in your substrate?",
        "options": ["Ignore it", "Remove the contaminated substrate immediately", "Add more water", "Increase temperature"],
        "answer": "Remove the contaminated substrate immediately",
        "difficulty": "beginner",
        "explanation": "Contaminated substrate should be removed quickly to prevent spreading to healthy cultures.",
        "topic": "cultivation_process"
    },
    {
        "question": "What does 'breaking and shaking' accomplish in spawn production?",
        "options": ["Damages the mycelium", "Distributes mycelium evenly and speeds colonization", "Adds nutrients", "Increases humidity"],
        "answer": "Distributes mycelium evenly and speeds colonization",
        "difficulty": "intermediate",
        "explanation": "Breaking up colonized spawn and shaking distributes growth points throughout the substrate.",
        "topic": "cultivation_process"
    },
    {
        "question": "What is the purpose of the 'shock' treatment for some mushroom substrates?",
        "options": ["To kill the mycelium", "To trigger fruiting by simulating natural conditions", "To add nutrients", "To increase colonization"],
        "answer": "To trigger fruiting by simulating natural conditions",
        "difficulty": "advanced",
        "explanation": "Cold shock or other treatments can simulate seasonal changes that trigger mushroom formation in nature.",
        "topic": "cultivation_process"
    },
    {
        "question": "How many flushes can you typically expect from one substrate?",
        "options": ["1 flush only", "2-4 flushes", "10+ flushes", "Unlimited flushes"],
        "answer": "2-4 flushes",
        "difficulty": "intermediate",
        "explanation": "Most substrates will produce 2-4 flushes before nutrients are depleted, with the first being largest.",
        "topic": "cultivation_process"
    },
    {
        "question": "What does 'sectoring' mean when working with mushroom cultures?",
        "options": ["Dividing harvest areas", "Isolating specific genetic strains", "Cutting substrate into pieces", "Creating growing zones"],
        "answer": "Isolating specific genetic strains",
        "difficulty": "advanced",
        "explanation": "Sectoring involves isolating and selecting specific mycelial growth sectors with desirable characteristics.",
        "topic": "cultivation_process"
    },
    {
        "question": "Which medicinal mushroom is most famous for supporting cognitive function and nerve health?",
        "options": ["Lion's Mane", "Reishi", "Cordyceps", "Turkey Tail"],
        "answer": "Lion's Mane",
        "difficulty": "intermediate",
        "explanation": "Lion's Mane contains compounds that may stimulate nerve growth factor (NGF) and support brain health.",
        "topic": "medicinal_mushrooms"
    },
    {
        "question": "What is the primary medicinal compound found in Turkey Tail mushrooms?",
        "options": ["Lentinan", "Polysaccharide-K (PSK)", "Ganoderic acid", "Hericenones"],
        "answer": "Polysaccharide-K (PSK)",
        "difficulty": "advanced",
        "explanation": "PSK from Turkey Tail is extensively studied for immune system support and is approved as a cancer treatment adjunct in Japan.",
        "topic": "medicinal_mushrooms"
    },
    {
        "question": "Which mushroom is traditionally used to boost energy and athletic performance?",
        "options": ["Reishi", "Cordyceps", "Shiitake", "Maitake"],
        "answer": "Cordyceps",
        "difficulty": "beginner",
        "explanation": "Cordyceps has been traditionally used to increase energy, stamina, and oxygen utilization.",
        "topic": "medicinal_mushrooms"
    },
    {
        "question": "What is Chaga mushroom primarily known for?",
        "options": ["High antioxidant content", "Protein content", "Fast growth rate", "Easy cultivation"],
        "answer": "High antioxidant content",
        "difficulty": "beginner",
        "explanation": "Chaga has one of the highest ORAC (antioxidant) values of any food, making it popular for anti-aging benefits.",
        "topic": "medicinal_mushrooms"
    },
    {
        "question": "Which compound in Shiitake mushrooms is known for immune system benefits?",
        "options": ["Lentinan", "PSK", "Ganoderic acid", "Ergosterol"],
        "answer": "Lentinan",
        "difficulty": "advanced",
        "explanation": "Lentinan is a beta-glucan extracted from Shiitake that has been extensively studied for immune support.",
        "topic": "medicinal_mushrooms"
    },
    {
        "question": "What is Maitake mushroom's nickname related to its medicinal properties?",
        "options": ["Dancing Mushroom", "Blood Sugar Mushroom", "Weight Loss Mushroom", "All of the above"],
        "answer": "All of the above",
        "difficulty": "intermediate",
        "explanation": "Maitake is called 'Dancing Mushroom' and is studied for blood sugar regulation and weight management support.",
        "topic": "medicinal_mushrooms"
    },
    {
        "question": "Which mushroom is known as the 'King of the Forest' and grows as a parasitic conk?",
        "options": ["Reishi", "Chaga", "Turkey Tail", "Lion's Mane"],
        "answer": "Chaga",
        "difficulty": "intermediate",
        "explanation": "Chaga grows as a black, charcoal-like conk on birch trees and is highly prized for its medicinal properties.",
        "topic": "medicinal_mushrooms"
    },
    {
        "question": "What makes Cordyceps unique among medicinal fungi?",
        "options": ["It's the largest mushroom", "It parasitizes insects in the wild", "It only grows in water", "It's the fastest growing"],
        "answer": "It parasitizes insects in the wild",
        "difficulty": "advanced",
        "explanation": "Wild Cordyceps sinensis grows by parasitizing caterpillar larvae, making it extremely rare and valuable.",
        "topic": "medicinal_mushrooms"
    },
    {
        "question": "Which mushroom is commonly called 'Nature's Xanax' for its calming properties?",
        "options": ["Lion's Mane", "Reishi", "Cordyceps", "Shiitake"],
        "answer": "Reishi",
        "difficulty": "beginner",
        "explanation": "Reishi is known for its adaptogenic and calming properties, often used to promote relaxation and better sleep.",
        "topic": "medicinal_mushrooms"
    },
    {
        "question": "What is the active compound in Lion's Mane that supports nerve growth?",
        "options": ["Hericenones and Erinacines", "Lentinan", "PSK", "Ganoderic acid"],
        "answer": "Hericenones and Erinacines",
        "difficulty": "advanced",
        "explanation": "These unique compounds in Lion's Mane can cross the blood-brain barrier and stimulate nerve growth factor production.",
        "topic": "medicinal_mushrooms"
    },
    {
        "question": "Which mushroom is being studied for its potential in treating neurodegenerative diseases?",
        "options": ["Turkey Tail", "Lion's Mane", "Cordyceps", "Maitake"],
        "answer": "Lion's Mane",
        "difficulty": "intermediate",
        "explanation": "Lion's Mane shows promise in research for Alzheimer's, Parkinson's, and other neurodegenerative conditions.",
        "topic": "medicinal_mushrooms"
    },
    {
        "question": "What is the traditional preparation method for Reishi mushrooms?",
        "options": ["Eaten fresh like vegetables", "Dried and made into tea or powder", "Fermented into alcohol", "Only used as substrate"],
        "answer": "Dried and made into tea or powder",
        "difficulty": "beginner",
        "explanation": "Reishi is too bitter and woody to eat fresh, so it's traditionally dried and prepared as teas, tinctures, or powders.",
        "topic": "medicinal_mushrooms"
    },
    {
        "question": "Which mushroom contains the highest concentration of beta-glucans?",
        "options": ["Button mushrooms", "Reishi", "Turkey Tail", "Enoki"],
        "answer": "Turkey Tail",
        "difficulty": "advanced",
        "explanation": "Turkey Tail contains up to 35-40% beta-glucans, one of the highest concentrations among medicinal mushrooms.",
        "topic": "medicinal_mushrooms"
    },
    {
        "question": "What is the scientific name for the Cordyceps species most commonly cultivated?",
        "options": ["Cordyceps sinensis", "Cordyceps militaris", "Cordyceps ophioglossoides", "Cordyceps capitata"],
        "answer": "Cordyceps militaris",
        "difficulty": "advanced",
        "explanation": "Cordyceps militaris is easier to cultivate than the wild C. sinensis and contains similar beneficial compounds.",
        "topic": "medicinal_mushrooms"
    },
    {
        "question": "Which medicinal mushroom is known for supporting liver health?",
        "options": ["Cordyceps", "Reishi", "Lion's Mane", "All of the above"],
        "answer": "All of the above",
        "difficulty": "intermediate",
        "explanation": "Many medicinal mushrooms, including Reishi, Cordyceps, and Lion's Mane, have compounds that support liver function.",
        "topic": "medicinal_mushrooms"
    }
]

def get_questions_by_difficulty(difficulty):
    """Filter questions based on chosen difficulty"""
    if difficulty == "mixed":
        return QUESTIONS
    else:
        return [q for q in QUESTIONS if q["difficulty"] == difficulty]

def get_questions_count():
    """Get total number of questions available"""
    return len(QUESTIONS)

def get_difficulty_distribution():
    """Get distribution of questions by difficulty level"""
    distribution = {"beginner": 0, "intermediate": 0, "advanced": 0}
    for question in QUESTIONS:
        distribution[question["difficulty"]] += 1
    return distribution

def get_topic_distribution():
    """Get distribution of questions by topic"""
    topics = {}
    for question in QUESTIONS:
        topic = question["topic"]
        topics[topic] = topics.get(topic, 0) + 1
    return topics

