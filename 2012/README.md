# Sight & Sound Poll Data
Data from the _Sound & Sound_ polls of the greatest films of all time conducted every decade.

For the 2012 poll, here is the time it took for me to scrape:
- the data of 1,205 voters (directors and critics) [[652 KB](https://github.com/serve-and-volley/sight-and-sound-poll-data/blob/main/2012/csv_raw_data/voters_2012.csv)]
- the data of the all 12,060 votes (some voters voted for more than 10 movies) [[1.2 MB](https://github.com/serve-and-volley/sight-and-sound-poll-data/blob/main/2012/csv_raw_data/votes_2012.csv)]

```bash
$ time python3 scrape_votes_2012.py

['558', 'Gulnara Abikeyeva', 'gulnara abikeyeva', 'critics poll', 'programmer', 'Art director, International Eurasia Film Festival', 'Kazakhstan', 'female', 10]
['1033', 'Lenny Abrahamson', 'lenny abrahamson', 'directors poll', 'Director', 'Garage; Adam and Paul', 'Ireland', 'male', 10]
['316', 'Mehmet Açar', 'mehmet acar', 'critics poll', 'critic', 'Critic, Haberturk', 'Turkey', 'male', 10]
['1090', 'Newton Aduaka', 'newton aduaka', 'directors poll', 'Director', 'Ezra; Rage', 'Nigerla', 'male', 10]
['624', 'Eva af Geijerstam', 'eva af geijerstam', 'critics poll', 'critic', 'Critic', 'Sweden', 'female', 10]
['444', 'Kaleem Aftab', 'kaleem aftab', 'critics poll', 'critic', 'Writer, the Independent, the National, Interview', 'UK', 'male', 10]
['855', 'Alejandro Agresti', 'alejandro agresti', 'directors poll', 'Director', 'Valentin; The Lake House', 'Argentina', 'male', 10]
['1115', 'Pedro Aguilera', 'pedro aguilera', 'directors poll', 'Director', 'La influencia; Shipwreck', 'Spain', 'male', 10]
['886', 'Ashim Ahluwalia', 'ashim ahluwalia', 'directors poll', 'Director', 'Miss Lovely; John & Jane ', 'India', 'male', 10]
['704', 'Daisuke Akasaka',  'daisuke akasaka', 'critics poll', 'Critic','Critic', 'Japan', 'male', 10]
⋮
['909', 'Chadi Zeneddine', 'chadi zeneddine', 'directors poll', 'Director', 'Falling from Earth ', 'Lebanon', 'male', 10]
['392', 'Ling Zhang', 'ling zhang', 'critics poll', 'academic', 'Ph.D student, Department of Cinema and Media Studies\nUniversity of Chicago', 'China', 'male', 10]
['919', "Cui Zi'en", "cui zi'en", 'directors poll', 'Director', "Men and Women; Queer China, 'Comrade China'", 'China', 'male', 10]
['94', 'Slavoj Zizek', 'slavoj zizek', 'critics poll', 'critic', 'Philosopher and cultural critic', 'Slovenia', 'male', 10]
['2', 'Zsolt Gyenge', 'zsolt gyenge', 'critics poll', 'academic', 'Assistant professor, Moholy-Nagy University of Art and Design, Budapest', 'Hungary', 'male', 10]
['362', 'Marco Ettore Zucchi', 'marco ettore zucchi', 'critics poll', 'critic', 'Film critic, RSI Radiotelevisione svizzera', 'Switzerland', 'male', 10]
['578', 'Gertjan Zuilhof', 'gertjan zuilhof', 'critics poll', 'programmer', 'Art historian; critic; curator and programmer for International Film Festival Rotterdam', 'Netherlands', 'male', 10]
['873', 'Andrzej Żuławski', 'andrzej zulawski', 'directors poll', 'Director', "Possession; L'important c'est d'aimer ", 'Poland', 'male', 10]
['116', 'Santos Zunzunegui', 'santos zunzunegui', 'critics poll', 'academic', 'Professor of History of Cinema, Basque Country University, UPV/EHU', 'Spain', 'male', 10]
['872', 'Andrey Zvyagintsev', 'andrey zvyagintsev', 'directors poll', 'Director', 'The Return; The Banishment', 'Russia', 'male', 10]

real    14m15.454s
user    1m24.433s
sys     0m5.708s
```

- The data of 2,421 films that have BFI film IDs:

```bash
$ time python3 scrape_films_2012.py
['4ce2b6938b54a', 'O Lucky Man!', 'o lucky man!', '', '', '1973', 'United Kingdom | USA', 'Comedy::Fantasy', 'Film', 'Fiction', 'Malcolm McDowell | Ralph Richardson | Rachel Roberts', 'malcolm mcdowell | ralph richardson | rachel roberts', 'Lucky Man | Coffee Man', 'lucky man | coffee man']
['4ce2b693a1a98', 'Le TEMPESTAIRE', 'le tempestaire', 'Jean Epstein', 'jean epstein', '1947', 'France', 'Fantasy', 'Film', 'Non Fiction', '', '', '', '']
['4ce2b693a235d', 'TERRA EM TRANSE', 'terra em transe', 'Glauber Rocha', 'glauber rocha', '1967', 'Brazil', 'Drama', 'Film', 'Fiction', 'Jardel Filho | José Lewgoy | Glauce Rocha', 'jardel filho | jose lewgoy | glauce rocha', 'LAND IN TRANCE | LAND IN TORMENT | LAND IN ANGUISH | EARTH ENTRANCED', 'land in trance | land in torment | land in anguish | earth entranced']
['4ce2b693a2ab4', 'T.G.: Psychic Rally in Heaven', 't.g.: psychic rally in heaven', 'Derek Jarman', 'derek jarman', '1981', 'United Kingdom', 'Performance', 'Film', 'Fiction', 'Throbbing Gristle | Genesis P. Orridge | Chris Carter', 'throbbing gristle | genesis p. orridge | chris carter', 'Throbbing Gristle | Psychic Rally in Heaven', 'throbbing gristle | psychic rally in heaven']
['4ce2b693b2c90', 'DOBRO POZHALOVAT', 'dobro pozhalovat', 'Elem Klimov', 'elem klimov', '1964', 'USSR', '', 'Film', 'Fiction', 'Vitya Kosykh | Evgeny Evstignyev | Lydia Smirnova', 'vitya kosykh | evgeny evstignyev | lydia smirnova', 'NO HOLIDAY FOR INOCHKIN | WELCOME | WELCOME OR NO ENTRY FOR UNAUTHORISED PERSONS', 'no holiday for inochkin | welcome | welcome or no entry for unauthorised persons']
['4ce2b693c9d98', "The Draughtsman's Contract", "the draughtsman's contract", '', '', '1982', 'United Kingdom', 'Period drama', 'Film', 'Fiction', 'Anthony Higgins | Janet Suzman | Anne Louise Lambert', 'anthony higgins | janet suzman | anne louise lambert', 'Meurtre Dans Un Jardin Anglais | Der Kontrakt Des Zeichners', 'meurtre dans un jardin anglais | der kontrakt des zeichners']
['4ce2b693ce4b7', 'Dune', 'dune', 'David Lynch', 'david lynch', '1984', 'USA', 'Science Fiction', 'Film', 'Fiction', 'The Vienna Symphony Orchestra | Francesca Annis | Leonardo Cimino', 'the vienna symphony orchestra | francesca annis | leonardo cimino', '', '']
['4ce2b693ec5ed', 'E.T.  The Extra-terrestrial', 'e.t.  the extra-terrestrial', 'Steven Spielberg', 'steven spielberg', '1982', 'USA', 'Science Fiction', 'Film', 'Fiction', 'Dee Wallace-Stone | Peter Coyote | Robert MacNaughton', 'dee wallace-stone | peter coyote | robert macnaughton', "E.T. and Me | A Boy's Life", "e.t. and me | a boy's life"]
['4ce2b69412f2f', 'FAITS DIVERS', 'faits divers', '', '', '1983', 'France', 'Documentary', 'Film', 'Non Fiction', '', '', 'NEWS ITEMS | MIXED REPORTS', 'news items | mixed reports']
['4ce2b69415af8', 'Fanny and Alexander', 'fanny and alexander', 'Ingmar Bergman', 'ingmar bergman', '1982', 'France | Sweden | Federal Republic of Germany', 'Drama', 'Television', 'Fiction', 'Kristina Adolphson | Börje Ahlstedt | Pernilla Allwin', 'kristina adolphson | borje ahlstedt | pernilla allwin', 'Fanny och Alexander | Fanny und Alexander | Fanny et Alexandre', 'fanny och alexander | fanny und alexander | fanny et alexandre']
⋮
['4f4bb332e9cf5', 'Wuthering Heights', 'wuthering heights', 'Andrea Arnold', 'andrea arnold', '2011', 'United Kingdom', 'Romance | Drama', 'Film', 'Fiction', 'Kaya Scodelario | James Howson | Solomon Glave', 'kaya scodelario | james howson | solomon glave', '', '']
['4f4bb44dd26c1', 'Margaret', 'margaret', 'Kenneth Lonergan', 'kenneth lonergan', '2011', 'USA', 'Drama', 'Film', 'Fiction', 'Anna Paquin | J. Smith-Cameron | Jean Reno', 'anna paquin | j. smith-cameron | jean reno', '', '']
['4f4bb49918aff', 'The Girl with the Dragon Tattoo', 'the girl with the dragon tattoo', 'David Fincher', 'david fincher', '2011', 'Sweden | USA', 'Thriller', 'Film', 'Fiction', 'Daniel Craig | Rooney Mara | Stellan Skarsgård', 'daniel craig | rooney mara | stellan skarsgard', '', '']
['4f4bb53687fa1', 'Martha Marcy May Marlene', 'martha marcy may marlene', 'Sean Durkin', 'sean durkin', '2011', '', 'Thriller', 'Film', 'Fiction', 'Elisabeth Olsen | Christopher Abbott | Brady Corbet', 'elisabeth olsen | christopher abbott | brady corbet', '', '']
['4f4bb60f049ad', 'Trishna', 'trishna', '', '', '2012', 'United Kingdom | India | Sweden', 'Drama', 'Film', 'Fiction', 'Freida Pinto | Riz Ahmed | Roshan Seth', 'freida pinto | riz ahmed | roshan seth', '', '']
['50c306d7d32dc', "Bir zamanlar Anadolu'da", "bir zamanlar anadolu'da", 'Nuri Bilge Ceylan', 'nuri bilge ceylan', '2011', 'Bosnia and Herzegovina | Turkey', 'Crime', 'Film', 'Fiction', 'Muhammet Uzuner | Yilmaz Erdogan | Taner Birsel', 'muhammet uzuner | yilmaz erdogan | taner birsel', 'Once upon a Time in Anatolia', 'once upon a time in anatolia']
['50c30ab0647b1', 'Amour', 'amour', 'Michael Haneke', 'michael haneke', '2012', 'Austria | France | Germany', 'Romance | Drama', 'Film', 'Fiction', 'Jean-Louis Trintignant | Emmanuele Riva | Isabelle Huppert', 'jean-louis trintignant | emmanuele riva | isabelle huppert', 'Love | Liebe', 'love | liebe']
['50c30c6d14136', 'Sandow', 'sandow', 'William Dickson', 'william dickson', '1894', 'USA', '', 'Film', 'Non Fiction', 'Eugen Sandow', 'eugen sandow', '', '']
['50c30c6e3cbeb', 'Petition', 'petition', 'Zhao Liang', 'zhao liang', '2009', '', '', 'Film', 'Non Fiction', '', '', 'Shangfang | La Cour des plaignants', 'shangfang | la cour des plaignants']
['50f8858778b62', 'Eniaios', 'eniaios', 'Gregory J. Markopoulos', 'gregory j. markopoulos', '1948', '', "Artists' Moving Image", 'Film', 'Non Fiction', '', '', '', '']

real    45m30.094s
user    2m10.987s
sys     0m7.929s
```

More documentation forthcoming.
