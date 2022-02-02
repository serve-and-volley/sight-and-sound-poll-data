# Sight & Sound Poll Data
Data from the _Sound & Sound_ polls of the greatest films of all time conducted every decade.

For the 2012 poll, here is the time it took for me to scrape:
- the data of 1,205 voters (directors and critics) [726 KB]
- the data of the all 12,060 votes (some voters voted for more than 10 movies) [1.26 MB]

```bash
$ time python3 scrape_votes_2012.py

['558', 'Gulnara Abikeyeva', 'programmer', 'Kazakhstan', 'Female', 'critics poll', 'Art director, International Eurasia Film Festival', 'Kazakhstan', 10]
['1033', 'Lenny Abrahamson', 'Director', 'Ireland', 'Male', 'directors poll', 'Garage; Adam and Paul', 'Ireland', 10]
['316', 'Mehmet Açar', 'critic', 'Turkey', 'Male', 'critics poll', 'Critic, Haberturk', 'Turkey', 10]
['1090', 'Newton Aduaka', 'Director', 'Nigerla', 'Male', 'directors poll', 'Ezra; Rage', 'Nigerla', 10]
['624', 'Eva af Geijerstam', 'critic', 'Sweden', 'Female', 'critics poll', 'Critic', 'Sweden', 10]
['444', 'Kaleem Aftab', 'critic', 'UK', 'Male', 'critics poll', 'Writer, the Independent, the National, Interview', 'UK', 10]
['855', 'Alejandro Agresti', 'Director', 'Argentina', 'Male', 'directors poll', 'Valentin; The Lake House', 'Argentina', 10]
['1115', 'Pedro Aguilera', 'Director', 'Spain', 'Male', 'directors poll', 'La influencia; Shipwreck', 'Spain', 10]
['886', 'Ashim Ahluwalia', 'Director', 'India', 'Male', 'directors poll', 'Miss Lovely; John & Jane ', 'India', 10]
['704', 'Daisuke Akasaka', 'Critic', 'Japan', 'Male', 'critics poll', 'Critic', 'Japan', 10]

⋮
['909', 'Chadi Zeneddine', 'Director', 'Lebanon', 'Male', 'directors poll', 'Falling from Earth ', 'Lebanon', 10]
['392', 'Ling Zhang', 'academic', 'China', 'Male', 'critics poll', 'Ph.D student, Department of Cinema and Media Studies\nUniversity of Chicago', 'China', 10]
['919', "Cui Zi'en", 'Director', 'China', 'Male', 'directors poll', "Men and Women; Queer China, 'Comrade China'", 'China', 10]
['94', 'Slavoj Zizek', 'critic', 'Slovenia', 'Male', 'critics poll', 'Philosopher and cultural critic', 'Slovenia', 10]
['2', 'Zsolt Gyenge', 'academic', 'Hungary', 'Male', 'critics poll', 'Assistant professor, Moholy-Nagy University of Art and Design, Budapest', 'Hungary', 10]
['362', 'Marco Ettore Zucchi', 'critic', 'Switzerland', 'Male', 'critics poll', 'Film critic, RSI Radiotelevisione svizzera', 'Switzerland', 10]
['578', 'Gertjan Zuilhof', 'programmer', 'Netherlands', 'Male', 'critics poll', 'Art historian; critic; curator and programmer for International Film Festival Rotterdam', 'Netherlands', 10]
['873', 'Andrzej Żuławski', 'Director', 'Poland', 'Male', 'directors poll', "Possession; L'important c'est d'aimer ", 'Poland', 10]
['116', 'Santos Zunzunegui', 'academic', 'Spain', 'Male', 'critics poll', 'Professor of History of Cinema, Basque Country University, UPV/EHU', 'Spain', 10]
['872', 'Andrey Zvyagintsev', 'Director', 'Russia', 'Male', 'directors poll', 'The Return; The Banishment', 'Russia', 10]

real    18m37.720s
user    2m1.502s
sys     0m6.656s
```

More documentation forthcoming.
