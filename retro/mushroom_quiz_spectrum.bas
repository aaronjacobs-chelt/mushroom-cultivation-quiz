10 REM ************************************
20 REM * MUSHROOM CULTIVATION QUIZ v1.1  *
30 REM * ZX SPECTRUM BASIC VERSION       *
40 REM * BY AARON J - 2025               *
50 REM ************************************
60 REM
70 REM INITIALIZE VARIABLES
80 LET SCORE = 0
90 LET TOTAL = 0
100 LET Q = 0: REM QUESTION COUNTER
110 DIM Q$(20,60): REM QUESTIONS
120 DIM A$(20,4,20): REM ANSWERS (4 PER QUESTION)
130 DIM C$(20,20): REM CORRECT ANSWERS
140 DIM E$(20,80): REM EXPLANATIONS
150 REM
160 REM SETUP SCREEN
170 BORDER 4: PAPER 0: INK 7: CLS
180 PRINT AT 2,8;"MUSHROOM CULTIVATION"
190 PRINT AT 3,14;"QUIZ"
200 PRINT AT 5,4;"ZX SPECTRUM BASIC VERSION"
210 PRINT AT 7,12;"BY AARON J"
220 PRINT AT 9,8;"PRESS ANY KEY TO START"
230 PAUSE 0
240 CLS
250 REM
260 REM LOAD QUESTIONS INTO ARRAYS
270 GOSUB 2000: REM LOAD QUESTION DATA
280 REM
290 REM MAIN MENU
300 CLS
310 PRINT "MUSHROOM CULTIVATION QUIZ"
320 PRINT "========================="
330 PRINT
340 PRINT "CHOOSE DIFFICULTY:"
350 PRINT "1. BEGINNER (5 QUESTIONS)"
360 PRINT "2. INTERMEDIATE (8 QUESTIONS)"
370 PRINT "3. ADVANCED (5 QUESTIONS)"
380 PRINT "4. EXIT"
390 PRINT
400 INPUT "ENTER CHOICE (1-4): ";CHOICE
410 IF CHOICE < 1 OR CHOICE > 4 THEN GOTO 400
420 IF CHOICE = 4 THEN GOTO 1900
430 REM
440 REM SET DIFFICULTY PARAMETERS
450 IF CHOICE = 1 THEN LET D$ = "BEGINNER": LET QMAX = 5: LET QSTART = 1
460 IF CHOICE = 2 THEN LET D$ = "INTERMEDIATE": LET QMAX = 8: LET QSTART = 6
470 IF CHOICE = 3 THEN LET D$ = "ADVANCED": LET QMAX = 5: LET QSTART = 14
480 REM
490 REM START QUIZ
500 CLS
510 PRINT "STARTING "; D$; " QUIZ"
520 PRINT "======================="
530 PRINT
540 PRINT "YOU WILL ANSWER "; QMAX; " QUESTIONS"
550 PRINT "PRESS ANY KEY WHEN READY..."
560 PAUSE 0
570 REM
580 REM QUIZ LOOP
590 FOR Q = QSTART TO QSTART + QMAX - 1
600   GOSUB 1000: REM DISPLAY QUESTION
610   GOSUB 1200: REM GET ANSWER
620   GOSUB 1400: REM CHECK ANSWER
630 NEXT Q
640 REM
650 REM SHOW FINAL SCORE
660 CLS
670 PRINT "QUIZ COMPLETE!"
680 PRINT "=============="
690 PRINT
700 PRINT "YOUR SCORE: "; SCORE; " OUT OF "; QMAX
710 LET PERCENT = INT(SCORE * 100 / QMAX)
720 PRINT "PERCENTAGE: "; PERCENT; "%"
730 PRINT
740 IF PERCENT >= 80 THEN PRINT "EXCELLENT! MUSHROOM MASTER!"
750 IF PERCENT >= 60 AND PERCENT < 80 THEN PRINT "GOOD! FUNGI EXPERT!"
760 IF PERCENT >= 40 AND PERCENT < 60 THEN PRINT "OK! KEEP STUDYING!"
770 IF PERCENT < 40 THEN PRINT "POOR! MORE PRACTICE NEEDED!"
780 PRINT
790 PRINT "PRESS ANY KEY FOR MENU..."
800 PAUSE 0
810 GOTO 290: REM BACK TO MENU
820 REM
830 REM ===========================
840 REM SUBROUTINES
850 REM ===========================
860 REM
870 REM DISPLAY QUESTION SUBROUTINE
1000 CLS
1010 PRINT "QUESTION "; Q - QSTART + 1; " OF "; QMAX
1020 PRINT "DIFFICULTY: "; D$
1030 PRINT "========================"
1040 PRINT
1050 PRINT Q$(Q)
1060 PRINT
1070 FOR I = 1 TO 4
1080   PRINT I; ". "; A$(Q,I)
1090 NEXT I
1100 PRINT
1110 RETURN
1120 REM
1130 REM GET ANSWER SUBROUTINE
1200 INPUT "YOUR ANSWER (1-4): "; ANS
1210 IF ANS < 1 OR ANS > 4 THEN PRINT "INVALID! TRY AGAIN.": GOTO 1200
1220 LET USER$ = A$(Q,ANS)
1230 RETURN
1240 REM
1250 REM CHECK ANSWER SUBROUTINE
1400 LET TOTAL = TOTAL + 1
1410 IF USER$ = C$(Q) THEN GO TO 1413
1411 LET CORRECT =0
1412 GO TO 1415
1413 LET SCORE = SCORE + 1
1414 LET CORRECT = 1
1415 REM Continue...
1420 PRINT
1430 IF CORRECT = 1 THEN PRINT "CORRECT! WELL DONE!"
1440 IF CORRECT = 0 THEN PRINT "WRONG! CORRECT ANSWER: "; C$(Q)
1450 PRINT
1460 PRINT "EXPLANATION:"
1470 PRINT E$(Q)
1480 PRINT
1490 PRINT "PRESS ANY KEY TO CONTINUE..."
1500 PAUSE 0
1510 RETURN
1520 REM
1530 REM EXIT ROUTINE
1900 CLS
1910 PRINT "THANKS FOR PLAYING!"
1920 PRINT "HAPPY MUSHROOM GROWING!"
1930 PAUSE 0 : NEW
1940 REM
1950 REM ===========================
1960 REM QUESTION DATA
1970 REM ===========================
1980 REM
1990 REM LOAD QUESTION DATA SUBROUTINE
2000 REM BEGINNER QUESTIONS (1-5)
2010 LET Q$(1) = "What is mycelium?"
2020 LET A$(1,1) = "A type of mushroom"
2030 LET A$(1,2) = "The root system of fungi"
2040 LET A$(1,3) = "A growing substrate"
2050 LET A$(1,4) = "A sterilization method"
2060 LET C$(1) = "The root system of fungi"
2070 LET E$(1) = "Mycelium is the vegetative part of fungi, consisting of branching thread-like structures."
2080 REM
2090 LET Q$(2) = "Which is the best beginner mushroom to grow?"
2100 LET A$(2,1) = "Shiitake"
2110 LET A$(2,2) = "Oyster mushrooms"
2120 LET A$(2,3) = "Morel"
2130 LET A$(2,4) = "Chanterelle"
2140 LET C$(2) = "Oyster mushrooms"
2150 LET E$(2) = "Oyster mushrooms are hardy, fast-growing, and tolerant of varying conditions."
2160 REM
2170 LET Q$(3) = "What temperature range is ideal for most mushrooms?"
2180 LET A$(3,1) = "5-10deg C"
2190 LET A$(3,2) = "15-25deg C"
2200 LET A$(3,3) = "30-40deg C"
2210 LET A$(3,4) = "45-55deg C"
2220 LET C$(3) = "15-25deg C"
2230 LET E$(3) = "Most cultivated mushrooms thrive in moderate temperatures between 15-25deg C."
2240 REM
2250 LET Q$(4) = "What is the ideal humidity for mushroom growing?"
2260 LET A$(4,1) = "30-40%"
2270 LET A$(4,2) = "50-60%"
2280 LET A$(4,3) = "80-95%"
2290 LET A$(4,4) = "100%"
2300 LET C$(4) = "80-95%"
2310 LET E$(4) = "High humidity (80-95%) is essential for proper mushroom development and growth."
2320 REM
2330 LET Q$(5) = "What does 'pinning' mean in mushroom cultivation?"
2340 LET A$(5,1) = "Securing the growing medium"
2350 LET A$(5,2) = "Initial mushroom formation"
2360 LET A$(5,3) = "Harvesting process"
2370 LET A$(5,4) = "Sterilization technique"
2380 LET C$(5) = "Initial mushroom formation"
2390 LET E$(5) = "Pinning is when tiny mushroom pins (baby mushrooms) first appear on the substrate."
2400 REM
2410 REM INTERMEDIATE QUESTIONS (6-13)
2420 LET Q$(6) = "What is the purpose of sterilization in mushroom growing?"
2430 LET A$(6,1) = "To add nutrients"
2440 LET A$(6,2) = "To kill competing organisms"
2450 LET A$(6,3) = "To increase moisture"
2460 LET A$(6,4) = "To improve texture"
2470 LET C$(6) = "To kill competing organisms"
2480 LET E$(6) = "Sterilization eliminates bacteria, molds, and other contaminants that compete with mushrooms."
2490 REM
2500 LET Q$(7) = "What is a fruiting chamber?"
2510 LET A$(7,1) = "A harvesting container"
2520 LET A$(7,2) = "A controlled environment for mushroom growth"
2530 LET A$(7,3) = "A storage facility"
2540 LET A$(7,4) = "A compost bin"
2550 LET C$(7) = "A controlled environment for mushroom growth"
2560 LET E$(7) = "A fruiting chamber maintains optimal humidity, temperature, and air exchange for mushrooms."
2570 REM
2580 LET Q$(8) = "Which substrate is commonly used for oyster mushrooms?"
2590 LET A$(8,1) = "Pure sand"
2600 LET A$(8,2) = "Straw"
2610 LET A$(8,3) = "Concrete"
2620 LET A$(8,4) = "Metal shavings"
2630 LET C$(8) = "Straw"
2640 LET E$(8) = "Straw is an excellent, readily available substrate for growing oyster mushrooms."
2650 REM
2660 LET Q$(9) = "What does 'inoculation' mean?"
2670 LET A$(9,1) = "Harvesting mushrooms"
2680 LET A$(9,2) = "Adding spawn to substrate"
2690 LET A$(9,3) = "Cleaning equipment"
2700 LET A$(9,4) = "Drying mushrooms"
2710 LET C$(9) = "Adding spawn to substrate"
2720 LET E$(9) = "Inoculation is the process of introducing mushroom spawn into the growing substrate."
2730 REM
2740 LET Q$(10) = "How long does oyster mushroom colonization typically take?"
2750 LET A$(10,1) = "1-3 days"
2760 LET A$(10,2) = "1-2 weeks"
2770 LET A$(10,3) = "2-3 months"
2780 LET A$(10,4) = "1 year"
2790 LET C$(10) = "1-2 weeks"
2800 LET E$(10) = "Oyster mushrooms typically colonize their substrate within 1-2 weeks under proper conditions."
2810 REM
2820 LET Q$(11) = "What is spawn in mushroom cultivation?"
2830 LET A$(11,1) = "Baby mushrooms"
2840 LET A$(11,2) = "Mushroom seeds"
2850 LET A$(11,3) = "Mycelium on a carrier medium"
2860 LET A$(11,4) = "Harvested mushrooms"
2870 LET C$(11) = "Mycelium on a carrier medium"
2880 LET E$(11) = "Spawn is mycelium grown on materials like grain, used to inoculate substrates."
2890 REM
2900 LET Q$(12) = "Why is fresh air exchange important?"
2910 LET A$(12,1) = "To prevent CO2 buildup"
2920 LET A$(12,2) = "To add moisture"
2930 LET A$(12,3) = "To increase temperature"
2940 LET A$(12,4) = "To add nutrients"
2950 LET C$(12) = "To prevent CO2 buildup"
2960 LET E$(12) = "Fresh air exchange prevents CO2 accumulation which can inhibit proper mushroom formation."
2970 REM
2980 LET Q$(13) = "What are shiitake mushrooms typically grown on?"
2990 LET A$(13,1) = "Plastic bags"
3000 LET A$(13,2) = "Hardwood logs or sawdust"
3010 LET A$(13,3) = "Metal containers"
3020 LET A$(13,4) = "Glass jars"
3030 LET C$(13) = "Hardwood logs or sawdust"
3040 LET E$(13) = "Shiitake mushrooms naturally grow on hardwood and are cultivated on logs or sawdust."
3050 REM
3060 REM ADVANCED QUESTIONS (14-18)
3070 LET Q$(14) = "What is the optimal pH range for most mushroom substrates?"
3080 LET A$(14,1) = "3.0-4.0"
3090 LET A$(14,2) = "6.0-7.0"
3100 LET A$(14,3) = "8.0-9.0"
3110 LET A$(14,4) = "10.0-11.0"
3120 LET C$(14) = "6.0-7.0"
3130 LET E$(14) = "Most mushrooms prefer slightly acidic to neutral pH conditions around 6.0-7.0."
3140 REM
3150 LET Q$(15) = "What is the purpose of casing soil?"
3160 LET A$(15,1) = "To add nutrients"
3170 LET A$(15,2) = "To trigger fruiting"
3180 LET A$(15,3) = "To sterilize substrate"
3190 LET A$(15,4) = "To store mushrooms"
3200 LET C$(15) = "To trigger fruiting"
3210 LET E$(15) = "Casing soil provides the moisture and microclimate that triggers mushroom pin formation."
3220 REM
3230 LET Q$(16) = "Which mushroom is known for its medicinal properties?"
3240 LET A$(16,1) = "Button mushroom"
3250 LET A$(16,2) = "Reishi"
3260 LET A$(16,3) = "Portobello"
3270 LET A$(16,4) = "Cremini"
3280 LET C$(16) = "Reishi"
3290 LET E$(16) = "Reishi is renowned for its immune-boosting and stress-reducing medicinal properties."
3300 REM
3310 LET Q$(17) = "What causes mushroom contamination most commonly?"
3320 LET A$(17,1) = "Too much water"
3330 LET A$(17,2) = "Poor sterile technique"
3340 LET A$(17,3) = "Wrong temperature"
3350 LET A$(17,4) = "Too much light"
3360 LET C$(17) = "Poor sterile technique"
3370 LET E$(17) = "Most contamination results from inadequate sterilization and poor sterile technique."
3380 REM
3390 LET Q$(18) = "What is the typical shelf life of fresh mushrooms?"
3400 LET A$(18,1) = "1-2 days"
3410 LET A$(18,2) = "5-7 days"
3420 LET A$(18,3) = "2-3 weeks"
3430 LET A$(18,4) = "1-2 months"
3440 LET C$(18) = "5-7 days"
3450 LET E$(18) = "Fresh mushrooms typically last 5-7 days when stored properly in the refrigerator."
3460 REM
3470 RETURN
9999 SAVE "MushQuiz" LINE 10
