# start adding different questions in the form of strings here
# right now it is in a csv file I need to organize so try to use that
# sorry for the bad organization so far. 
questions = {
    "EXAMPLE QUESTIONS GO HERE" : "EXAMPLE ANSWERS GO HERE",
    "TESTING SOME QUESTIONS RN" : "RIGHT ANSWERS OVER HERE",
    "HELLO FELLOW HUMAN BEINGS" : "SOMETHING ELSE FOR USER",
    "HERE AS WELL WHY NOT /-/-" : "ZzzzZzzzZzzzZzzzZzzZzzZ"
}

# A more organized version of the csv file would look like this:
# Passage 1: "The Friendly Owl"

# Once upon a time, in a quiet forest, there lived a wise and friendly owl named Oliver. Oliver 
# loved to read books, especially about the stars and planets. Every night, he would sit on his 
# favorite branch and look up at the sky, hoping to catch a glimpse of a shooting star.

# Question 1: What was the owl's name?

# A) Oscar
# B) Oliver
# C) Otto
# D) Olivia
# Answer: B) Oliver

# **Passage 2: "The Rainbow"

# After a morning rain shower, Sarah saw a beautiful rainbow in the sky. It had seven different 
# colors, and it arched across the entire sky. Sarah was amazed by its beauty and wondered how it 
# was formed.

# Question 2: How many colors are there in a rainbow?

# A) 5
# B) 6
# C) 7
# D) 8
# Answer: C) 7

# **Passage 3: "The Enchanted Forest"

# In the middle of the Enchanted Forest, there was a hidden waterfall. The water from the waterfall 
# was crystal clear and sparkled like diamonds in the sunlight. Many animals visited the waterfall 
# to drink water and cool off on hot days.

# Question 3: What was special about the water in the Enchanted Forest's waterfall?

# A) It was purple.
# B) It was made of chocolate.
# C) It was crystal clear and sparkled like diamonds.
# D) It was red and bubbly.
# Answer: C) It was crystal clear and sparkled like diamonds.

# **Passage 4: "The Magic Book"

# Lucy found a dusty old book in her attic. As she opened it, a cloud of glittering dust swirled around 
# her. The book had a magical story inside, and it transported her to a land of talking animals and 
# colorful adventures.

# Question 4: What happened when Lucy opened the old book?

# A) She found a recipe for chocolate cake.
# B) A cloud of glittering dust swirled around her.
# C) She fell asleep.
# D) She met a famous scientist.
# Answer: B) A cloud of glittering dust swirled around her.


# Testing out how to get random questions and answers here if you want to look at it then just run this file
if __name__ == "__main__":
    import random as rand

    question = rand.choice(list(questions.keys()))
    answer = questions[question]

    # Generate a list of random answers and exclude the correct answer to not repeat choices
    answer_list = list(questions.values())
    answer_list.remove(answer)
    random_choices = rand.sample(answer_list, 3)

    # Add the correct answer to the list of choices at a random position
    random_position = rand.randint(0, len(random_choices))
    random_choices.insert(random_position, answer)

    print("Question:", question)
    print("\nChoose the correct answer:")
    for i, choice in enumerate(random_choices, 1):
        print(f"{i}. {choice}")

    print()
    print(answer)
    print("answer:", random_position + 1)

    choice = int(input("\nAnswer the question correctly for a treat: "))
    
    if choice == random_position + 1:
        print("yay you are right but I lied about the treat sorry")
    else:
        print("You're wrong. How could you. You said you were smart. You lied to me. Now I can never trust you. Please get out of my life. I don't ever want to see you here. And if I ever see you walking around here again, I will make sure you regret that decision. Just go away. Stop reading this. Stop I said. I'm dialing 911. Hello 911 this crazy guy won't go away. Yes I've asked him to go away many times but he refuses. What do you mean there is nothing you can do? They're harrassing me. Help me I feel unsafe with their presence near me. Why even have a job if you can't help me. Ok well that failed, so I guess you can stay here?? I don't really know what to do now. I expected you to leave a long time ago. Umm well I guess I'll tell you a story to pass the time because I have nothing else to do. Once upon a time, there was this magical you know what this is too boring. Half the pages in this book are gone anyways. So storytime is over I guess. Well I guess you win. I really thought we could be friends but nevermind. You know all you had to do was answer the question correctly. Those questions were meant for young children. Like the age of a 12 year old child or something like that. You are a grown adult getting these easy questions wrong. I think that really says something about you, something bad. You're dumb. I don't even care if you stay anymore because at least I know I'm not the dumbest person here. Honestly that makes me feel good about myself knowing I would never get that answer wrong. What do you mean I would get the answer wrong? Want to bet on that? Ok find lets try it. Ok let me get my reading glasses real quick its hard to see. Ok question 1 umm these answer choices don't make any sense to me. How am I supposed to know what color an orange is? I haven't eaten an orange in so long. Ummm I guess I'll guess this one. Oh I'm wrong? You know what this game is rigged I don't care about what you say. I am still smarter and I always will be. My IQ is 1,000,000,000,000 times bigger than yours. I would know because you probably don't even know how to even say that number. My IQ is so big even scientists who specialize in this kind of research can't begin to fathom how big it is. I know all the secrets and can solve any question that has an answer. The question I got wrong was not wrong, instead the game was wrong, either that or there was no correct answer to begin with. No it's not orange. I would know if an orange is oran... oh wait a minute. No stop get away from here. I HAVE A GUN GET AWAY FROM ME. I DON'T CARE ANYMORE I WANT YOU OUT OF HERE. Oh crap I didn't mean to fire it. Oh no what am I going to do. The blood is getting everywhere. I need to find somewhere to hide it. Oh this is a huge mess what am I going to do? Ok here is a trash bag let me just stuff this in here. Perfect it fits. Now I need to carefully sneak this to the forest. First let me mop up this blood. Ok great now it's time to sneak this filth out of here. Oh this thing is heavy, who would've known a body was this heavy to carry. Why are you so fat... Ok this might be a bit harder than I thought. Let me try drag this I guess. Ok that works better. Now time to open the car. Place the body in the back. Ok there should be a shovel somewhere, althought I don't remember where exactly I kept a shovel. Let me check out back. Here it is! The good old trusty shovel. And here we go off to an adventure. I should've filled this car with gas it's getting low. Ehh it can't hurt to stop for some gas. It's not like anyone can see the body anyways. Unleaded obviously I need to get my money's worth out of this gas. Ok great now its time to head back into the woods. Oh crap there is a police pulling me over. I knew I shouldn't have ran that red light. Just keep calm and don't act like there is a dead body in the back of my car. You got this. Hello officer is there a reason I was pulled over? Oh I'm sorry I didn't realize I was going that fast, I just didn't see any signs telling me the speed limit so I just took a guess. Officer please I was in a hurry to do something I didn't realize I was going 60 over. Wait no please I don't need to get out of the car. Just let it slide. No I don't have any drugs and I do not consent to a search. Hey you can't do that this is against my rights. Run. I need to run. I think he knows. Where am I going to go. This is bad why did I have to shoot that dumb person. Why did I ever give them those questions that were obviously rigged. Why is the author of this story wasting time typing this instead of working on the game he is supposed to work on. Wait the author of the story! The guy typing this right now. Hey you yeah you typing this. Please change the story to have a happy ending. It can't end like this. I have a family and children who want to see me. Well maybe not I guess I am lonely but that's not my fault you made me into some random person with no life. You did this to me so please I will forgive you for making my life miserable if you can change this story around. Make sure the police isn't chasing after me or anyone in general remembers what happened today. Just go back into to story and make it to where I just left instead of shooting that person. Please this is the only favor I will ask of you. Wait no why are there dogs, I see them. I've got to run faster. Please stop doing this I will do anything. Get the dogs away and don't let them catch me please. I don't want things to end like this. I have a lot of life ahead of me to live on. Ow my leg. Charlie horse. The cramps I can't move it's to painful. Why, why did you do this to me. I hope you feel good about yourself. Because I wouldn't if I were you. I guess this is it. I guess this is where I say goodbye or I get taken to prison. Wait I have the gun on me I forgot. I guess there is only one way to get out of here. Either they catch me and who knows what will happen to me next, or I can end things forever. I think that will be a better choice. Well I guess this is it. If you are reading this I just want to let you know whoever typed this is not to be trusted and they are a terrible human being. This deserve to be dead and nothing good come out of them. Wait what am I talking about the person who is reading this is dead I killed them. Well if you are somehow alive or in the afterlife reading this, then I hope you forgive me for shooting you I didn't mean to. I just got bit mad you know that I have a short temper. Well I guess this is it. I'm going to do it. Anyday now. Come on just press the trigger you know you have nothing to live for. Why are you stalling and making this dumb story longer. The author of this story has homework and projects to do. Just end it so he can do something other than writing this dumb story that was just supposed to print soemthing small and simple to see if the user chose the wrong answer. Why are you writing this to begin with. Ok I think I'll end the story here then because there is nothing else I can really think about that can stall this story any longer than saying that I am stalling the story by not ending my life. On the count of 3. 1. 2. 3. #$&^@^*!&@*%(&&#@%@. Ok well I hope you enjoyed this dumb story I wrote because I was bored and needed a break from programming. Well that's if you read this entire story. If you read this entire story than I want to say congratulations but at the same time that is kind of sad that you had nothing better to do in your life so you chose to sit down and read this entire story rather than just typing clear in the terminal to get rid of this story and move on. Or cls if you are on windows it doesn't really matter. It actually surprises me how much I wrote. I don't think I've ever written something this long. Right now it is at column 7795. That is a lot of letters. I don't even think I've tried this hard to write something on a class like English where it really mattered. But to be honest, this was just some random pesron yapping about random stuff so I guess I didn't really try this hard. Instead it was just me being bored and typing random stuff that came from the top of my head. Well I'll go back to working now because that is more important than whatever this is. Bye :)")