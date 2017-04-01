from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, ReadingList, Book

engine = create_engine('sqlite:///readinglistwithusers.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="Robo Reader", email="tinnyTim@udacity.com",
             picture='http://pix.iemoji.com/images/emoji/apple/ios-9/256/grinning-face.png')
session.add(User1)
session.commit()

# List for Harry Potter
readinglist1 = ReadingList(user_id=1, name="The Harry Potter Series",
    description="The ultimate fantasy series of our time, featuring the Boy who Lived.")

session.add(readinglist1)
session.commit()

book1 = Book(user_id=1, name="Harry Potter and the Sorcerer's Stone", category="Fiction",
    author_first_name="J.K.", author_last_name="Rowling",
    description="""Harry Potter has no idea how famous he is. That's because he's being raised by his miserable aunt and uncle who are terrified Harry will learn that he's really a wizard, just as his parents were. But everything changes when Harry is summoned to attend an infamous school for wizards, and he begins to discover some clues about his illustrious birthright. From the surprising way he is greeted by a lovable giant, to the unique curriculum and colorful faculty at his unusual school, Harry finds himself drawn deep inside a mystical world he never knew existed and closer to his own noble destiny.""",
    website="https://www.amazon.com/Harry-Potter-Sorcerers-Stone-Rowling/dp/059035342X",
    reading_list=readinglist1)

session.add(book1)
session.commit()

book2 = Book(user_id=1, name="Harry Potter and the Chamber of Secrets", category="Fiction",
    author_first_name="J.K.", author_last_name="Rowling",
    description="""The Dursleys were so mean that hideous that summer that all Harry Potter wanted was to get back to the Hogwarts School for Witchcraft and Wizardry. But just as he's packing his bags, Harry receives a warning from a strange, impish creature named Dobby who says that if Harry Potter returns to Hogwarts, disaster will strike. And strike it does. For in Harry's second year at Hogwarts, fresh torments and horrors arise, including an outrageously stuck-up new professor, Gilderoy Lockheart, a spirit named Moaning Myrtle who haunts the girls' bathroom, and the unwanted attentions of Ron Weasley's younger sister, Ginny.""",
    website="https://www.amazon.com/Harry-Potter-Chamber-Secrets-Rowling/dp/0439064872",
    reading_list=readinglist1)

session.add(book2)
session.commit()

book3 = Book(user_id=1, name="Harry Potter and the Prisoner of Azkaban", category="Fiction",
    author_first_name="J.K.", author_last_name="Rowling",
    description="""For twelve long years, the dread fortress of Azkaban held an infamous prisoner named Sirius Black. Convicted of killing thirteen people with a single curse, he was said to be the heir apparent to the Dark Lord, Voldemort. Now he has escaped, leaving only two clues as to where he might be headed: Harry Potter's defeat of You-Know-Who was Black's downfall as well. And the Azkban guards heard Black muttering in his sleep, "He's at Hogwarts...he's at Hogwarts." Harry Potter isn't safe, not even within the walls of his magical school, surrounded by his friends. Because on top of it all, there may well be a traitor in their midst.""",
    website="https://www.amazon.com/Harry-Potter-Prisoner-Azkaban-Rowling/dp/0439136369",
    reading_list=readinglist1)

session.add(book3)
session.commit()

book4 = Book(user_id=1, name="Harry Potter and the Goblet of Fire", category="Fiction",
    author_first_name="J.K.", author_last_name="Rowling",
    description="""Harry Potter is midway through his training as a wizard and his coming of age. Harry wants to get away from the pernicious Dursleys and go to the International Quidditch Cup. He wants to find out about the mysterious event that's supposed to take place at Hogwarts this year, an event involving two other rival schools of magic, and a competition that hasn't happened for a hundred years. He wants to be a normal, fourteen-year-old wizard. But unfortunately for Harry Potter, he's not normal - even by wizarding standards. And in his case, different can be deadly.""",
    website="https://www.amazon.com/Harry-Potter-Goblet-Fire-Rowling/dp/0439139600",
    reading_list=readinglist1)

session.add(book4)
session.commit()

book5 = Book(user_id=1, name="Harry Potter and the Order of the Phoenix", category="Fiction",
    author_first_name="J.K.", author_last_name="Rowling",
    description="""In his fifth year at Hogwart's, Harry faces challenges at every turn, from the dark threat of He-Who-Must-Not-Be-Named and the unreliability of the government of the magical world to the rise of Ron Weasley as the keeper of the Gryffindor Quidditch Team. Along the way he learns about the strength of his friends, the fierceness of his enemies, and the meaning of sacrifice.""",
    website="https://www.amazon.com/Harry-Potter-Order-Phoenix-Rowling/dp/0439358078",
    reading_list=readinglist1)

session.add(book5)
session.commit()

book6 = Book(user_id=1, name="Harry Potter and the Half-Blood Prince", category="Fiction",
    author_first_name="J.K.", author_last_name="Rowling",
    description="""The war against Voldemort is not going well; even the Muggles have been affected. Dumbledore is absent from Hogwarts for long stretches of time, and the Order of the Phoenix has already suffered losses. And yet...as with all wars, life goes on. Sixth-year students learn to Apparate. Teenagers flirt and fight and fall in love. Harry receives some extraordinary help in Potions from the mysterious Half-Blood Prince. And with Dumbledore's guidance, he seeks out the full, complex story of the boy who became Lord Voldemort -- and thus finds what may be his only vulnerability.""",
    website="https://www.amazon.com/Harry-Potter-Half-Blood-Prince-Book/dp/0439785960",
    reading_list=readinglist1)

session.add(book6)
session.commit()

book7 = Book(user_id=1, name="Harry Potter and the Deathly Hallows", category="Fiction",
    author_first_name="J.K.", author_last_name="Rowling",
    description="""Readers beware. The brilliant, breathtaking conclusion to J.K. Rowling's spellbinding series is not for the faint of heart--such revelations, battles, and betrayals await in Harry Potter and the Deathly Hallows that no fan will make it to the end unscathed. Luckily, Rowling has prepped loyal readers for the end of her series by doling out increasingly dark and dangerous tales of magic and mystery, shot through with lessons about honor and contempt, love and loss, and right and wrong. Fear not, you will find no spoilers in our review--to tell the plot would ruin the journey, and Harry Potter and the Deathly Hallows is an odyssey the likes of which Rowling's fans have not yet seen, and are not likely to forget. But we would be remiss if we did not offer one small suggestion before you embark on your final adventure with Harry--bring plenty of tissues.""",
    website="https://www.amazon.com/Harry-Potter-Deathly-Hallows-Book/dp/0545139708",
    reading_list=readinglist1)

session.add(book7)
session.commit()


readinglist2 = ReadingList(user_id=1, name="Foreign Policy and the Presidency",
    description="Books chronicling foreign policy and the decisions presidents faced.")

session.add(readinglist2)
session.commit()

book1 = Book(user_id=1, name="Team of Rivals: The Political Genius of Abraham Lincoln", category="Non-Fiction",
    author_first_name="Doris Kearns", author_last_name="Goodwin",
    description="""This brilliant multiple biography is centered on Lincoln's mastery of men and how it shaped the most significant presidency in the nation's history.""",
    website="https://www.amazon.com/Team-Rivals-Political-Abraham-Lincoln/dp/0743270754",
    reading_list=readinglist2)

session.add(book1)
session.commit()

book2 = Book(user_id=1, name="The Woman Behind the New Deal: The Life and Legacy of Frances Perkins, Social Security, Unemployment Insurance, and the Minimum Wage", category="Non-Fiction",
    author_first_name="Kristin", author_last_name="Downey",
    description="""One of Franklin Delano Roosevelt's closest friends and the first female secretary of labor, Perkins capitalized on the president's political savvy and popularity to enact most of the Depression-era programs that are today considered essential parts of the country's social safety network.""",
    website="https://www.amazon.com/Woman-Behind-New-Deal-Unemployment/dp/1400078563",
    reading_list=readinglist2)

session.add(book2)
session.commit()

book3 = Book(user_id=1, name="One Hell of a Gamble: Khrushchev, Castro, and Kennedy, 1958-1964: The Secret History of the Cuban Missile Crisis", category="Non-Fiction",
    author_first_name="Aleksandr", author_last_name="Fursenko",
    description="""This important and controversial book draws the missing half of the story from secret Soviet archives revealed exclusively by the authors, including the files of Nikita Khrushchev and his leadership circle. Contained in these remarkable documents are the details of over forty secret meetings between Robert Kennedy and his Soviet contact, records of Castro's first solicitation of Soviet favor, and the plans, suspicions, and strategies of Khrushchev. This unique research opportunity has allowed the authors to tell the complete, fascinating, and terrifying story of the most dangerous days of the last half-century.""",
    website="https://www.amazon.com/One-Hell-Gamble-Khrushchev-1958-1964/dp/0393317900",
    reading_list=readinglist2)

session.add(book3)
session.commit()

book4 = Book(user_id=1, name="Manhunt: The Ten-Year Search for Bin Laden from 9/11 to Abbottabad", category="Non-Fiction",
    author_first_name="Peter", author_last_name="Bergen",
    description="""In Manhunt, Peter Bergen delivers a taut yet panoramic account of the pursuit and killing of Osama bin Laden. Here are riveting new details of bin Laden's flight after the crushing defeat of the Taliban to Tora Bora, where American forces came startlingly close to capturing him, and of the fugitive leader's attempts to find a secure hiding place. As the only journalist to gain access to bin Laden's Abbottabad compound before the Pakistani government demolished it, Bergen paints a vivid picture of bin Laden's grim, Spartan life in hiding and his struggle to maintain control of al-Qaeda. Half a world away, Bergen takes us inside the Situation Room, where President Obama considers the courses of action presented by his war council and receives conflicting advice from his top advisors before deciding to risk the raid that would change history--and then inside the Joint Special Ops Command, whose "secret warriors," the SEALs, would execute Operation Neptune Spear. From the moment two Black Hawks take off from Afghanistan until bin Laden utters his last words, Manhunt reads like a thriller.""",
    website="https://www.amazon.com/Manhunt-Ten-Year-Search-Laden-Abbottabad/dp/0307955885",
    reading_list=readinglist2)

session.add(book4)
session.commit()

book5 = Book(user_id=1, name="A World in Disarray: American Foreign Policy and the Crisis of the Old Order", category="Non-Fiction",
    author_first_name="Richard", author_last_name="Haass",
    description="""An examination of a world increasingly defined by disorder and a United States unable to shape the world in its image, from the president of the Council on Foreign Relations.""",
    website="https://www.amazon.com/World-Disarray-American-Foreign-Policy/dp/0399562362",
    reading_list=readinglist2)

session.add(book5)
session.commit()

readinglist3 = ReadingList(user_id=1, name="Coming of Age Novels",
    description="Stories about the transition from youth to adulthood.")

session.add(readinglist3)
session.commit()

book1 = Book(user_id=1, name="Great Expectations", category="Fiction",
    author_first_name="Charles", author_last_name="Dickens",
    description="""Great Expectations is a bildungsroman, or a coming-of-age novel, and it is a classic work of Victorian literature. It depicts the growth and personal development of an orphan named Pip. The novel was first published in serial form in Dickens's weekly periodical All the Year Round, from 1 December 1860 to August 1861.""",
    website="https://www.amazon.com/Great-Expectations-Charles-Dickens/dp/1503275183",
    reading_list=readinglist3)

session.add(book1)
session.commit()

book2 = Book(user_id=1, name="The Hunger Games", category="Fiction",
    author_first_name="Suzanne", author_last_name="Collins",
    description="""In the ruins of a place once known as North America lies the nation of Panem, a shining Capitol surrounded by twelve outlying districts. Long ago the districts waged war on the Capitol and were defeated. As part of the surrender terms, each district agreed to send one boy and one girl to appear in an annual televised event called, "The Hunger Games," a fight to the death on live TV. Sixteen-year-old Katniss Everdeen, who lives alone with her mother and younger sister, regards it as a death sentence when she is forced to represent her district in the Games. The terrain, rules, and level of audience participation may change but one thing is constant: kill or be killed.""",
    website="https://www.amazon.com/Hunger-Games-Book-1/dp/0439023521",
    reading_list=readinglist3)

session.add(book2)
session.commit()

book3 = Book(user_id=1, name="To Kill a Mockingbird", category="Fiction",
    author_first_name="Harper", author_last_name="Lee",
    description="""The unforgettable novel of a childhood in a sleepy Southern town and the crisis of conscience that rocked it, To Kill A Mockingbird became both an instant bestseller and a critical success when it was first published in 1960. It went on to win the Pulitzer Prize in 1961 and was later made into an Academy Award-winning film, also a classic. Compassionate, dramatic, and deeply moving, To Kill A Mockingbird takes readers to the roots of human behavior - to innocence and experience, kindness and cruelty, love and hatred, humor and pathos.""",
    website="https://www.amazon.com/Kill-Mockingbird-Harper-Lee/dp/0446310786",
    reading_list=readinglist3)

session.add(book3)
session.commit()

print "added reading list items!"