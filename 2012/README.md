# Sight & Sound Poll Data
Data from the _Sound & Sound_ polls of the greatest films of all time conducted every decade.

For the 2012 poll, here is the time it took for me to scrape:
- the data of 1,205 voters (directors and critics) [726 KB]
- the data of the all 12,060 votes (some voters voted for more than 10 movies) [1.26 MB]

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

More documentation forthcoming.
