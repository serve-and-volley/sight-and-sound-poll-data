# Sight & Sound Poll Data
Data from the _Sound & Sound_ polls of the greatest films of all time conducted every decade.

For the 2012 poll, here is the time it took for me to scrape:
- the data of 1,205 voters (directors and critics) [726 KB]
- the data of the all 12,060 votes (some voters voted for more than 10 movies) [1.26 MB]

```bash
$ time python3 voters_and_votes_2012.py
['Gulnara Abikeyeva', '558', 'programmer', 'Kazakhstan', 'Female', 'critics poll', 'Art director, International Eurasia Film Festival', 'Kazakhstan', 10]
['Lenny Abrahamson', '1033', 'Director', 'Ireland', 'Male', 'directors poll', 'Garage; Adam and Paul', 'Ireland', 10]
['Mehmet Açar', '316', 'critic', 'Turkey', 'Male', 'critics poll', 'Critic, Haberturk', 'Turkey', 10]
['Newton Aduaka', '1090', 'Director', 'Nigerla', 'Male', 'directors poll', 'Ezra; Rage', 'Nigerla', 10]
['Eva af Geijerstam', '624', 'critic', 'Sweden', 'Female', 'critics poll', 'Critic', 'Sweden', 10]
['Kaleem Aftab', '444', 'critic', 'UK', 'Male', 'critics poll', 'Writer, the Independent, the National, Interview', 'UK', 10]
['Alejandro Agresti', '855', 'Director', 'Argentina', 'Male', 'directors poll', 'Valentin; The Lake House', 'Argentina', 10]
['Pedro Aguilera', '1115', 'Director', 'Spain', 'Male', 'directors poll', 'La influencia; Shipwreck', 'Spain', 10]
['Ashim Ahluwalia', '886', 'Director', 'India', 'Male', 'directors poll', 'Miss Lovely; John & Jane ', 'India', 10]
['Daisuke Akasaka', '704', 'Critic', 'Japan', 'Male', 'critics poll', 'Critic', 'Japan', 10]
⋮
['Chadi Zeneddine', '909', 'Director', 'Lebanon', 'Male', 'directors poll', 'Falling from Earth ', 'Lebanon', 10]
['Ling Zhang', '392', 'academic', 'China', 'Male', 'critics poll', 'Ph.D student, Department of Cinema and Media Studies\nUniversity of Chicago', 'China', 10]
["Cui Zi'en", '919', 'Director', 'China', 'Male', 'directors poll', "Men and Women; Queer China, 'Comrade China'", 'China', 10]
['Slavoj Zizek', '94', 'critic', 'Slovenia', 'Male', 'critics poll', 'Philosopher and cultural critic', 'Slovenia', 10]
['Zsolt Gyenge', '2', 'academic', 'Hungary', 'Male', 'critics poll', 'Assistant professor, Moholy-Nagy University of Art and Design, Budapest', 'Hungary', 10]
['Marco Ettore Zucchi', '362', 'critic', 'Switzerland', 'Male', 'critics poll', 'Film critic, RSI Radiotelevisione svizzera', 'Switzerland', 10]
['Gertjan Zuilhof', '578', 'programmer', 'Netherlands', 'Male', 'critics poll', 'Art historian; critic; curator and programmer for International Film Festival Rotterdam', 'Netherlands', 10]
['Andrzej Żuławski', '873', 'Director', 'Poland', 'Male', 'directors poll', "Possession; L'important c'est d'aimer ", 'Poland', 10]
['Santos Zunzunegui', '116', 'academic', 'Spain', 'Male', 'critics poll', 'Professor of History of Cinema, Basque Country University, UPV/EHU', 'Spain', 10]
['Andrey Zvyagintsev', '872', 'Director', 'Russia', 'Male', 'directors poll', 'The Return; The Banishment', 'Russia', 10]

real    16m48.471s
user    2m16.952s
sys     0m7.435s
```

More documentation forthcoming.
