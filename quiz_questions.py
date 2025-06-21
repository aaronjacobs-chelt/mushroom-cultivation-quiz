#!/usr/bin/env python3
"""
Quiz Questions Database
Contains all mushroom cultivation quiz questions organized by difficulty and topic
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

