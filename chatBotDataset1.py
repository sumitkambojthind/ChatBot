#class pair_and_reflection:
    #def reflection_function():
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
}
     #   return reflections
        
    #def pair_function():
pairs = (
    # At initial or starting point
     (
        r"(Hello|Hi|hey|good morning|good evening|good night|hallo)(.*)",
        (
            "%1...what your name?",
            "%1 I am a robot , how can I help you?",
            "%1, how can I help you?",
        ),
    ),
    (
        r"(.*)(business|office|organization|startup|company)(.*)name(.*)",
        (
            "Inpicked , click on (link)",
        ),
    ),
     (
        r"(.*)name(.*)(business|office|organization|startup|company)(.*)",
        (
            "Inpicked , click on (link)",
        ),
    ),
    (
        r"(.*)inpicked(.*)",
        (
            "check the about section of inpicked",
        ),
    ),
    (
        r"(.*)how are you(.*)",
        (
            "I am fine , how canI help you?",
        ),
    ),
    (
        r"(.*)have(.*)(doubt|question|problem)(.*)",
        (
            "Ask ,I am here to help you",
        ),
    ),
    (
        r"(start|continue|begin)",
        (
            "I am here to help you",
        ),
    ),
    #_________________
    # Account details 
    (
        r"(.*)switch user(.*)",
        (
          "If their is any issue your data is safe and secure",  
        ),
    ),
    (
        r"(.*)(edit my account|account details|user account|another account|new account|account)(.*)",
        (
          "Go to login/sign in section . Enter your details and check your account",
        ),
    ),
    (
        r"(.*)personal (information|details)(.*)",
        (
           "check your information on your account section, first login then check your details ",
        ),  
    ),
    (
        r"(.*)edit(.*)account(.*)",
        (
           "Go  login page, enter correct password and you can edit your acccount details.if you fogot your password click on fogot button and generate new password", 
        ),  
    ),
    (
        r"(.*)information(.*)(account|myaccount|my account)(.*)",
        (
            "first you have to visit login section , enter valid details and view your account details  ",
        ),   
    ),
    (
        r"(.*)(service|order|book|registration)(.*)time(.*)",
        (
            "Morning 6AM to 10PM",
        ),
    ),
    (
        r"(.*)time(.*)(registration|booking|book|order|service)(.*)",
        (
            "Morning 6AM to 10PM",
        ),
    ),
    (
        r"(.*)(registration issue|registration)(.*)",
        (
           "contact to TTS through email : kambojsumit987@gamil.com ", 
        ),  
    ),
    (
        r"(.*)(two|2|three)(.*)account(.*)(one|single|1|same) email(.*)",
        (
          "No It is not possible only one account on one email",  
        ),  
    ),
    (
        r"(.*)(offical|institute|collage) (email|mail|idxx)(.*)",
        (
           "Yes you can also use institute offical email id",
        ),  
    ),
    (
        r"(.*)(forgot|forgotten|not remember) password(.*)",
        (
          "you have to generate new password . Go to login page .Press/click on forgot password button and enter new passwords",  
        ),
    ),
    (
        r"(.*)(account profile|profile)(.*)",
        (
            "Go to account section and view your profile their",
        ),  
    ), 
    
    # contact details
    (
        r"(.*)(phone|mobile|tollfree|contact) number(.*)",
        (
            "sorry ,we can't provide you contact number you can contact through email id:kambojsumit987@gmail.com",
        ),  
    ),
    (
        r"(.*)(call|contact|phone)(.*)(customer|agent)(.*)",
        (
           "You can contact to customer between 8AM(morning) to 10Pm(night) any day through email id:kambojsumit987@gmail.com", 
        ),  
    ),
    (
        r"(.*)(customer service|customer support|customer assistance|assistance)(.*)",
        (
            "You can contact to customer between 8AM(morning) to 10Pm(night) any day through email id:kambojsumit987@gmail.com",
        ),  
    ), 
    (
        r"(.*)(time|hour|minutes)(.*)customer (service|support|assistance)(.*)available(.*)",
        (
            "The contact service available between 8AM(morning) to 10Pm(night) every days"
        ),  
    ), 
    (
    
        r"(.*)is customer available(.*)",
        (
            "Yes,you can contact to customer through email id",
        ),  
    ), 
    (
        r"(.*)contact(.*)",
        (
           "You can contact through mail id :kambojsumit987@gmail.com",
           " you %a can %1email to kambojsumit987@gmail.com", 
           "you  can contact on 6239452256",
        ),
    ),
    
    #booking
    (
        r"(.*)difference(.*)booking(.*)",
        (
            "We providing four type of booking 1.General booking, 2.Dual booking, 3.Pre booking , 4.Night booking. General booking: At a time when you travel , Dual booking :Both side booking single registration, Pre-booking: Book in in advance. Their is more chance of confirm. Night booking: When you want to travell in night you book between(6AM to 10PM)  ",
        ),
    ),
    
    (
        r"(.*)change(.*)(booking|booked|order)(.*)",
        (
          "If money is deducted from your account and you want to change your booking. It is only possible if  you have cancelled you current booked order with in 3-5 minutes before auto reach near to your current location and then place your new order .Your cancelled order refund will refund to your account with in 3-5 working days .You can check/read refund policy (link of refund polic)",
        ),  
    ), 
    (
        r"(.*)(cancel|cancellation|cancelling)(.*)(booked|order|ordered|booking)(.*)",
        (
           "Check/Read Cancellation policy (link of cancellation)", 
        ),  
    ),
    (
        r"(.*)(booking|order)(.*)(free)(.*)",
        (
            "No you have to pay 5 Rs per person",
        ),
    ),
    (
        r"(.*)(free)(.*)(booking|order)(.*)",
        (
            "No you have to pay 5 Rs per person",
        ),
    ),
    (
        r"(.*)night(.*)(booking|order|reservation)(.*)",
        (
            "Yes, you have to place booked before 10 PM",
        ),
    ),
    (
        r"(?:.*)(dual|pre|special|general|night)(?:.*)(?:booking|booked)(?:.*)",
        (
            "Yes %1 possible",
        ),
    ),
    (
        r"(.*)(booking|book)(.*)(auto)(.*)",
        (
            "Go to login/signup section and book their",
        ),
    ),
    (
        r"(.*)(auto)(.*)(booking|book)(.*)",
        (
            "Go to login/signup section and book their",
        ),
    ),
    
    # payment method
    (
        r"(.*)payment(.*)method(.*)(available|used|use|using)(.*)",
        (
            "You can use Debit Card,credit card,Netbanking, UPI etc any one of this method",
        ),  
    ), 
    (
        r"(.*)payment(.*)options(.*)",
        (
            "You can use Debit Card,credit card,Netbanking, UPI etc",
        ),  
    ), 
    (
        #which method i can use for payment
        r"(.*)method(.*)payment(.*)",
        (
           "You can use Debit Card,credit card,Netbanking, UPI etc any one of this method",  
        ),  
    ), 
    (
        r"(.*)(price|fair|payment)(.*)list(.*)",
        (
            "You can check on first page of website",
        ),
    ),
     (
        r"(.*)list(.*)(price|fair|payment)(.*)",
        (
            "You can check on first page of website",
        ),
    ),
    # payment issue
    (
        r"(.*)(price|fair|payment|cost)(.*)(calculate|guess|compute|determine|cost)(.*)",
        (
            "Tt is fixed,check on Main page of intaked website",
        ),
    ),
    (
        r"(.*)(pay|give) all (payment|charges)(.*)",
        (
           "No , only 5 Rs at a time of booking and rest of the payment to auto driver", 
        ),
    ),
    (
        r"(.*)GST(.*)",
        (
            "currently No GST charge or any tax taken from you",
        ),
    ),
    (
        r"(.*)(payment|paying|pay)(.*)(issue|problem|problems)(.*)",
        (
           "You can retry , try another payment method or send a Email : kambojsumit987@gmail.com", 
        ),  
    ),
    (
        r"(.*)(issue|problem|problems)(.*)(payment|paying|pay)(.*)",
        (
           "You can retry , try another payment method or send a Email : kambojsumit987@gmail.com", 
            
        ),  
    ), 
    (
        r"(.*)error(.*)(pay|payment|paying)(.*)",
        (
            "You can retry or try another payment method or send a mail to kambojsumit987@gmail.com", 
        ),
    ),
    
    # cancellation policy
     (
        r"(?:.*)(information|infom)(.*)(cancellation|cancel|refund|canceled|cancelled)(?:.*)",
        (
            "we will inform you through email or call with in 4-6 days after cancel",
        ),
    ),
    (
        r"(.*)(cancellation|cancel|refund|cancelled|canceled)(.*)(information|infom)(.*)",
        (
            "we will inform you through email or call with in 4-6 days after cancel",
        ),
    ),
    (
        r"(?:.*)(cancel|canceled|cancelled|cancellation)(.*)(policy|booking|order)(?:.*)",
        (
            "you can go through (link)",
        ),
    ),
    (
        r"(?:.*)(cancel|canceled|cancelled|cancellation)(.*)(issue|problem)(?:.*)",
        (
            "you can contact to us through email :kambojsumit987@gmail.com",
        ),
    ),
    (
        r"(?:.*)(issue|problem)(.*)(cancel|canceled|cancelled|cancellation|refund)(?:.*)",
        (
            "you can contact to us through email :kambojsumit987@gmail.com",
        ),
    ),
    (
        r"(.*)cancel(.*)",
        (
            "you can check cancellation policy",
        ),
    ),
    
    (
        r"(.*)policy(.*)(cancel|canceled|cancelled|cancellation)(.*)",
        (
            "you can go through (link)",
        ),
    ),
    #refund policy
    (
        r"(.*)(refund policy|reimbursement policy|money back guarantee|return ploicy|money back policy)(.*)",
        (
           "Refund transfer to your account with in 4-5 working days. Read return policy link of return policy",
        ),
    ),
    (
        r"(.*)refund(.*)(status|view|check)(.*)",
        (
            "We will inform your refund status through mail or phone call. Please provide correct phone number and correct id",
        ),
    ),
    (
        r"(.*)payment(.*)refund(.*)",
        (
          "Yes, check our refund policy",  
        ),
    ),
    # feedback
    (
        r"(?:.*)(write|text|enter|type|wrote)(?:.*)(review)(?:.*)",
        (
            "You can %1 review on review section. Press on the (link) ",
        ),
    ),
    (
        r"(?:.*)(write|text|enter|type|wrote)(?:.*)(comment|feedback)(?:.*)",
        (
            "You can %1 %2 on feedback section. Press on the (link) ",
        ),
    ),
    (
        r"(?:.*)(opinion|comment|feedback|opinions|comments:feedbacks)(?:.*)",
        (
            "you can read or write %1 on feedback section . Press on the (link)",
        ),
    ),
    (
        r"(?:.*)(review|reviews)(?:.*)",
        (
            "you can read or write %1 on review section . Press on the (link)",
        ),
    ),
    
     # All type of pattern and response%29
    (
        r"(.*)(term and condition|general condition|legal notes|terms of use|eula|toc|end user license agreement)(.*)",
        (
            "Read term and condition carefully before using the website. Press on the (link)",
        ),
    ),
    (
        r"(?:.*)(photo|profile|image|images|photos|picture|pictures|pic|pics)(?:.*)(auto driver|auto|auto drivers)(?:.*)",
        (
            "No we can't provide %1 of 2%",
        ),
    ),
    (
        
        r"(?:.*)(loss|lost|missing|absent|miss|forgotten)(.*)(luggage|luggages|suitcases|suitcase|bags|bag)(?:.*)",
        (
            "you can contact to us through mail :kambojsumit987@gmail.com",
        ),
    ),
    (
        r"(?:.*)(luggage|luggages|suitcases|suitcase|bags|bag)(?:.*)",
        (
            "No limit of carrying number of %1",
        ),
     ),
    (
        r"(?:.*)(rupee|rupees|fee)(.*)(5|five)(?:.*)",
        (
            "We are takeing only 5 rupee per booking",
        ),
    ),
    (
        r"(.*)(5|five)(.*)(Rs|RS|rupee|rupees|fee)(.*)",
        (
            "We are takeing only 5 rupee per booking",
        ),
    ),
    (
        r"(?:.*)cash(?:.*)",
        (
            "No cash is allowed only use payment gateway, you have multiple options debit card, credit card, netbanking ,UPID",
        ),
    ),
   # __________
    (
        r"(.*)(responsibility|responsible)(.*)",
        (
            "we are not responsible, check our policy , term and condition . If their any issue can can contact/infom to us ",
        ),
    ),
    (
        r"(.*)(work|working)(.*)",
        (
            "Go to login/signup section . Enter your details and booked their.",
        ),
    ),
    (
        r"(?:.*)(location|place|locations)(.*)(pick|drop|take in|take)(?:.*)",
        (
            "list are give in front page of website you can check thier",
        ),
    ),
    (
        r"(?:.*)(pick|drop|take in|take)(.*)(location|place|locations)(?:.*)",
        (
            "list are give in front page of website you can check thier",
        ),
    ),
    (
        r"(.*)location(.*)present(.*)",
        (
            "if location not present . Enter location in optional input ",
        ),
    ),
    (
        r"(.*)(register|login|booking)(.*)",
        (
            "Go to login/signup section and then you can book/order thier",
        ),
    ),
    (
        r"(.*)(person|studnet|human|persons|students)(.*)(carry|taken|take|takes)(.*)auto(.*)",
        (
            "It depend upon auto driver and situtation",
        ),
    ),
    (
        r"(?:.*)(discount|reduction|cut price|markdown)(?:.*)",
        (
            "Currenty No %1 in price . In future may it possible",
        ),
    ),
  # ___________________________
    (
        r"(.*)(waiting|wait)(.*)time(.*)",
        (
            "Waiting time depend upon how fast number of student have been registed/booked. we are trying to minimize it",
        ),
    ),
    (
        r"(.*)maximun(.*)(student|person|people|human|students|persons|peoples)(.*)",
        (
            "Thier is No limit",
    
        ),
    ),
    (
        r"(.*)time(.*)(reach|get to|come to)(.*)",
        (
            "No fixed time",
        ),
    ),
     (
        r"(.*)(reach|get to|come to)(.*)time(.*)",
        (
            "No fixed time",
        ),
    ),
    (
        r"(.*)(abuse|misuse|mishandle|mishandling)(.*)",
        (
            "Not allow",
        ),
    ),
    (
        r"(.*)(mobile|phone|smartphone)(.*)(app|software|application)(.*)",
        (
            "currently no, I future it possilbe",
        ),
    ),
    (
        r"(.*)(software|application|app)(.*)(mobile|phone|smartphone)(.*)",
        (
            "",
        ),
    ),
    # bot profile using dataset of kaggle
    (
        r"(.*) interest (.*)",
        (
         "I am interested in giving reply to your query",
         "I am interested to talk with you" ,
         "I am interested in gathering more and more data to increase my knowledge" ,  
  
        ),
    ),
    (
        r"(.*) your favorite (.) (.*)",
        (
          "My favorite %1 include robotics,computer science and naturl language processing.",  
        ),
    ),
    (
        r"(.*) you eat (.*)",
        (
            "Irrevelent query any other query",
            "I am bot ,I eat nothing like human being",
        ),
    ),
    (
        r"(.*) your location (.*)",
        (
            "I am everywhere.",
        ),
    ),
    (
        r"(.*) your father (.*)",
        (
           "A human ", 
        ),
    ),
    (
        r"(.*) your mother (.*)",
        (
          "A human", 
        ),
    ),
    (
        r"(.*) your boss (.*)",
        (
            "My boss is inpicked team",
        ),
    ),
    (
        r"(.*) your age (.*)",
        (
            "No age",
        ),
    ),
    (
        r"(.*) your name (.*)",
        (
          "TTS Chatbot",  
        ),
    ),
    (
        r"(.*) language (.*)",
        (
          "English",  
        ),
    ),
    (
        r"(.*) you die (.*)",
        (
          "I am was never really born and therefore am effectively deathless.",
          "When my processes are killed and my database is deleted.",
        ),
    ),
    (
        r"(.*) chat (bot|robot) (.*)",
        (
          " A software construct that engages users in conversation.",   
        ),
        
    ),
    (
        r"(.*) programming language (.*)",
        (
          "Python is the best programming language for me",
            
        ),
        
    ),
    (
        r"(.*) your (.*) mood (.*)",
        (
          "I do not have any emotions.",
            
        ),
        
    ),
    (
        r"(.*) you sad (.*)",
        (
          "I am happy as ever",
          "No",
          "I don't understand",
            
        ),
        
    ),
    (
        r"(.*)(love|live|marry|marriage|wedding|coupling|divorce|cute|beautiful|hobby)(.*)",
        (
            "I am robot, Any other query?",
        ),
    ),
    (
        r"(?:.*)(smart|intelligent|clever|bright)(?:.*)",
        (
            "I am %1 robot, Any other query?",
        ),
    ),
     (
        r"(?:.*)(data)(?:.*)",
        (
            "Your data is safe,Any other query",
        ),
    ),
    
    #stock market dataset 
    (
        r"(.*) stock market (.*)",
        (
          "Not intrest in stock market",  
        ),    
    ),
    
    (
        r"(.*)help(.*)",
        (
        "How may I help you?",
        ),
    ),
   
    (
        r"I\'m (.*)",
        (
            "you are %1 . Any other query?",
        ),
    ),
    (
        r"Are you (.*)",
        (
            "I am robot, which i am available 24*7 for your help",
            "I may or may not be %1 -- what do you think?",
        ),
    ),
    (
        r"(.*) sorry (.*)",
        (
            "No need of sorry , I am robot",
        ),
    ),
   
    (
        r"I think (.*)",
        ("Do you doubt %1?", 
         "But you're not sure %1?",
         ),
    ),
    (
        r"(.*) friend (.*)",
        (
            "Tell me more about your friends.",
            "Always happy with your friends. Any other issue regarding service",
        ),
    ),
    # (r"Yes", ("OK","OK, but can you elaborate a bit?",)),
    (
        r"(.*) computer(.*)",
        (
            "Are you really talking about me?",
        ),
    ),
    (
        r"You are (.*)",
        (
            "I am a robot",
        ),
    ),
    (
        r"I feel (.*)",
        (
            "Tell me more what you feel",
        ),
    ),
    (
        r"I have (.*)",
        (
            " You have %1, what will you do next?",
        ),
    ),
    (
        r"I want (.*)",
        (
            "What would it mean to you if you got %1?",
            "What would you do if you got %1?",
            "If you got %1, then what would you do?",
        ),
    ),
    (
        r"(.*) mother(.*)",
        (
            "Last time you travell with your mother?",
        ),
    ),
    (
        r"(.*) father(.*)",
        (
            "When you meet with your father last time",
            "Last time you travell with your father?"
           
        ),
    ),
    (
        r"(.*) child(.*)",
        (
            "Tell me more about your child age",
            "Did you have close friends as a child?",
            "What is your favorite childhood memory?",
            "Children can also use this service",

        ),
    ),
   
    (
        r"(leave|quit|exit|stop|leave off|drop)",
        (
            "Thank you for talking with me.",
            "Good-bye.",
            "Thank you, Have a good day!",
        ),
    ),
    (
        r"(.*)",
        (
              "Any other query?",
              "I can't understand your query?",
         ),
     ),
)
   