# -*- coding: utf-8 -*-
import sys
import random
from clint.textui import colored


angry = ["(૭ ◉༬◉)૭⁾⁾⁾⁾"]
sad = ["( ≧Д≦)",
"((´д｀))",
"(∩︵∩)",
"(▰˘︹˘▰)",
"(✖╭╮✖)",
"(‘A`)",
"(︶︹︺)",
"(＠´＿｀＠)",
"（´＿｀）",
"(⊙︿⊙✿)",
"(⌣_⌣”)",
"(▰︶︹︺▰)",
"~(｡☉︵ ಠ@)&gt;",
"⊙︿⊙",
"ヽ(●ﾟ´Д｀ﾟ●)ﾉﾟ",
"(.﹒︣︿﹒︣.)",
"(Θ︹Θ)ს",
"٩꒰´·⌢•｀꒱۶⁼³₌₃",
":: ˓(ᑊᘩᑊ⁎) ::",
"˓˓(ᑊᘩᑊ⁎)",
"(๑◕︵◕๑)",
"( .. )",
"(｡•́︿•̀｡)",
"(´°ω°`)",
"੨( ･᷄ ︵･᷅ )ｼ",
"꒰๑˃͈꒳˂͈๑꒱ﾉ*ﾞ̥",
"(⌯˃̶᷄ ﹏ ˂̶᷄⌯)ﾟ",
"(っ- ‸ – ς)",
"(๑′°︿°๑)",
"⊛ठ̯⊛",
"ಠ╭╮ಠ",
"( ◞᷄દ◟᷅ )",
"(oꆤ︵ꆤo)",
"ಗಾ ﹏ ಗಾ",
"ᵟຶᴖ ᵟຶ",
"(⋅⃘˕̭⋅⃘)",
"ōۃō",
"( ⁍᷄⌢̻⁍᷅ )",
"(.﹒︠₋﹒︡.)",
"(˵¯͒⌢͗¯͒˵)",
"☹ै",
"(　´_ﾉ` )",
"ʕ ಡ ﹏ ಡ ʔ",
"●︿●",
"(◕︿◕✿)",
"ਉ_ਉ",
"༶ඬ༝ඬ༶",
"໒( •́ ∧ •̀ )७",
"へ[ •́ ‸ •̀ ]ʋ",
"┏༼ ◉ ╭╮ ◉༽┓",
"▐ ﹒︣ Ĺ̯ ﹒︣ ▐",
"( ˃̶͈ ̯ ̜ ˂̶͈ˊ ) ︠³",
"(๑´╹‸╹`๑)",
"(⌯˃̶᷄ ﹏ ˂̶᷄⌯)",
"（（●´∧｀●））",
"(｡-人-｡)",
"、ヽ｀(~д~*)、ヽ｀",
"(;*△*;)",
"（ ; ; ）",
"(っ˘̩╭╮˘̩)っ",
"(个_个)",
"（；へ：）",
"o(；△；)o",
"((o(;△;)o))",
"ͼ(ݓ_ݓ)ͽ",
"(*´；ェ；`*)",
"(´；ω；`)",
"(´；д；`)",
"(´；Д；｀)",
"(゜´Д｀゜)",
"ಥ_ಥ",
"(ఠ్ఠ ˓̭ ఠ్ఠ)",
"(๑′̥̥̥▵‵̥̥̥ ૂ๑)",
"(٭°̧̧̧꒳°̧̧̧٭)",
"（ｉДｉ）",
"( ´•̥×•̥` )",
"( ᵒ̴̶̷̥́ _ᵒ̴̶̷̣̥̀ )",
"( ˃̣̣̥ω˂̣̣̥ )",
"꒰๑•̥﹏•̥๑꒱",
"(੭ ˃̣̣̥ ㅂ˂̣̣̥)੭ु",
"( ɵ̥̥ ˑ̫ ɵ̥̥)",
"(´;︵;`)",
"( ´•̥̥̥ω•̥̥̥` )",
"(ˊ̥̥̥̥̥ ³ ˋ̥̥̥̥̥)",
"(⌯͒⁍̩̩᷄ ɪ ⁍̩̩᷄ฅ͒)",
"(๑ १д१)",
"(๑⃙⃘°̧̧̧ㅿ°̧̧̧๑⃙⃘)",
"(῭̩̩̩̥ꄗ΅̩̩̩̥)",
"(̥ ̥এ́ ̼ এ̥̀)̥̥",
"(̥ ̥এ́ ̼ এ̥̀)̥̥੭ੇʓ ੭ੇʓ",
"⁝(˚͈͈͈͈̥̆₍₎˚͈͈͈͈̥̆⁎)⁝",
"(;﹏;)",
"(˃̥̥ω˂̥̥̥)",
"( ͒˃̩̩⌂˂̩̩ ͒)",
"(ᵕ̣̣̣̣̣̣﹏ᵕ̣̣̣̣̣̣)",
"(˃̩̩̥ɷ˂̩̩̥)",
"( -̩̩̩͡˛ -̩̩̩͡ )",
"(﹡ᵗ ᵔ ᵗ ﹡)",
"( ب_ب )",
"c〳 ݓ ﹏ ݓ 〵੭",
"( Ĭ ^ Ĭ )",
"(´;ω;｀)",
"(;•͈́༚•͈̀)",
"＼（＠；◇；＠）／"]
evil = ["↜(͛ ꒪͒৫͏̈́꒪͒)͛⌰"]
food = ["( ˘▽˘)っ♨"]
excited = ["(ﾉ･ｪ･)ﾉ",
"(/^▽^)/",
"(ﾉ´ヮ´)ﾉ*:･ﾟ✧",
"(ﾉ≧∀≦)ﾉ",
"(ﾉ^ヮ^)ﾉ*:・ﾟ✧",
"(/ ‘з’)/",
"(۶ꈨຶꎁꈨຶ )۶ʸᵉᵃʰᵎ",
"⁽(◍˃̵͈̑ᴗ˂̵͈̑)⁽",
"(╯✧∇✧)╯",
"Σ(ノ°▽°)ノ",
"( ƅ°ਉ°)ƅ",
"ヽ(　･∀･)ﾉ",
"˭̡̞(◞⁎˃ᆺ˂)◞*✰",
"(p^-^)p",
"(ﾉ^∇^)ﾉﾟ",
"ヽ(〃･ω･)ﾉ",
"(۶* ‘ꆚ’)۶”",
"（。＞ω＜）。",
"（ﾉ｡≧◇≦）ﾉ",
"ヾ(｡･ω･)ｼ",
"(ﾉ･д･)ﾉ",
".+:｡(ﾉ･ω･)ﾉﾞ",
"Σ(*ﾉ´&gt;ω&lt;｡`)ﾉ",
"ヾ（〃＾∇＾）ﾉ♪",
".ﾟ☆(ノё∀ё)ノ☆ﾟ.",
"⌒ﾟ(❀&gt;◞౪◟&lt;)ﾟ⌒",
"ヽ/❀o ل͜ o\ﾉ",
"⤴︎ ε=ε=(ง ˃̶͈̀ᗨ˂̶͈́)۶ ⤴︎",
"୧༼✿ ͡◕ д ◕͡ ༽୨",
"＼（＠￣∇￣＠）／",
"＼(^▽^＠)ノ",
"ヾ(@^▽^@)ノ",
"(((＼（＠v＠）／)))",
"＼(*T▽T*)／",
"＼（＾▽＾）／",
"＼（Ｔ∇Ｔ）／",
"ヽ( ★ω★)ノ",
"ヽ(；▽；)ノ",
"ヾ(。◕ฺ∀◕ฺ)ノ",
"ヾ(＠† ▽ †＠）ノ",
"ヾ(＠^∇^＠)ノ",
"ヾ(＠^▽^＠)ﾉ",
"ヾ（＠＾▽＾＠）ノ",
"ヾ(＠゜▽゜＠）ノ",
"ヾ(@°▽°@)ノ",
"ヾ(＠°▽°＠)ﾉ",
"ヽ(*≧ω≦)ﾉ",
"ヽ(*⌒∇⌒*)ﾉ",
"ヽ(^。^)丿",
"ヽ(＾Д＾)ﾉ",
"ヽ(=^･ω･^=)丿",
"⸂⸂⸜(രᴗര๑)⸝⸃⸃",
"⸜(ّᶿധّᶿ)⸝",
"ヽ(｡･ω･｡)ﾉ",
"╰(‘ω’ )╯",
"╰(°ㅂ°)╯",
"┗(＾∀＾)┛",
"ヾ(๑’౪`๑)ﾉﾞ",
"ヾ(*Őฺ∀Őฺ*)ﾉ",
"╰(✧∇✧)╯",
"ヾ(๑⃙⃘´ꇴ｀๑⃙⃘)ﾉ",
"✯⸜(ّᶿ̷ധّᶿ̷)⸝✯",
"◦°˚\(´°౪°`)/˚°◦",
"\(-ㅂ-)/",
"◦°˚\(*❛‿❛)/˚°◦",
"╰(◉ᾥ◉)╯",
"⌒°(ᴖ◡ᴖ)°⌒",
"ヾ(´∀｀○)ﾉ",
"｡ﾟ✶ฺ.ヽ(*´∀`*)ﾉ.✶ฺﾟ｡",
"＼(;ﾟ∇ﾟ)/",
"ヽ(*´∀`)ﾉﾞ",
"⸂⸂⸜(ೆ௰ೆ๑)⸝⸃⸃",
"✧⁺⸜(●′▾‵●)⸝⁺✧",
"ヾ(`ω`　)/",
"◦°˚\☻/˚°◦",
"ヾ(｡^ω^｡)ノ",
"⸜(ّᶿॕധّᶿॕ)⸝",
"⸜(ؔᶿധؔᶿ)⸝",
"╰( ･ ᗜ ･ )╯",
"┏○ ＼(ﾟ 0ﾟ ;)/┓",
"\"҉*\( ‘ω’ )/*҉",
"ヽ(^◇^*)/",
"ヾ(≧∇≦)ゞ",
"*。ヾ(｡&gt;ｖ&lt;｡)ﾉﾞ*。",
"☆*~ﾟ⌒(‘-‘*)⌒ﾟ~*☆",
"ヽ(ﾟ∀ﾟ)ﾉ",
"ヾ(o≧∀≦o)ﾉﾞ",
".｡ﾟ+.ヽ| ゝ∀・*|ﾉ｡+.ﾟ",
"(ﾟ&lt;|＼(･ω･)／|&gt;ﾟ)",
"╰| ° ◞౪◟ ° |╯",
"ヽ༼&gt;ل͜&lt;༽ﾉ",
"ヽ[ヘ ل͟ ヘ]╯",
"＼(・ω・)/",
"ヽ（゜ω゜○）ノ",
"☆~~ヾ(&gt;▽&lt;)ﾉ｡･☆",
"＼（*´･∀･｀*）／",
"＼（゜э゜）／",
"ヾ(￣◇￣)ノ",
"ヾ【*≧д≦】ノ",
"ヽ(^O^)ノ",
"ヾ(´▽｀*)ﾉ☆",
"ヾ(・∀・｀*)ﾉ☆",
"☆ヾ(*´▽｀)ﾉ",
"☆ヾ(*´・∀・)ﾉ",
"ヾ(*・ω・)ノ",
"ヾ(・ω・*)ノ",
"ヽ( ´￢`)ﾉ",
"ヾ(≧∪≦*)ノ〃",
"ヾ(*ゝω・*)ノ",
"＼（○＾ω＾○）／",
"╰(*´︶`*)╯",
"ヽ( ´ー`)ノ",
"┝＼( ‘∇^*)^☆／┥",
"ヽ(^o^)丿",
"┗|⌒O⌒|┛",
"┗|・o・|┛",
"ヾ(●・◇・●)ノ",
"ヽ( ‘ω’ )ﾉ",
"((ヾ(* ´∀｀)ノ))",
"ヽ(´∇｀)ﾉ",
"･:*+.\(( °ω° ))/.:+",
"ヽ(^□^｡)ノ",
"ヾ(o✪‿✪o)ｼ",
"＼(*ﾟ∀ﾟ*)／",
"＼(*^￢^*)／",
"Ψ(≧ω≦)Ψ",
"ヽ(*≧л≦)ﾉ",
"⸜₍ᕏ͜⁎₎⸝",
"୧☉□☉୨",
"꒳ᵃ꒳ᵃ꒳ᵃ~(๑°ᗨૢ°๑)♡ӵᵉ੨ᑋ✧",
"✧*.◟(ˊᗨˋ)◞.*✧ᗯ੨~ɪ̊♪ْ˖⋆",
"о(ж＞▽＜)ｙ ☆",
"( ˃̶ω˂̶ ૃ)",
"(٭°̧̧̧ω°̧̧̧٭)",
"⸍⚙̥ꇴ⚙̥⸌",
"(⊙ꇴ⊙)",
"(*≧∀≦*)",
"(≧∇≦*)",
"（๑✧∀✧๑）",
"(★^O^★)",
"(ᗒᗨᗕ)",
"(⌯꒪͒ ꌂ̇ ꒪͒)",
"(≧∀≦)",
"(⌬̀⌄⌬́)",
"₊·*◟(˶╹̆ꇴ╹̆˵)◜‧*･",
"(ᗒᏬᗕ) ˡ̵˖✮⃛",
"(ؑ⸍⸍ᵕؑ̇⸍⸍)◞✧",
"✮⃛( ◞´•௰•`)✮⃛",
"(ؑᵒᵕؑ̇ᵒ)◞✧",
"₍₍ ◝(●˙꒳˙●)◜ ₎₎",
"(´｡✪ω✪｡｀)",
"｡;+*(★`∪´☆)*+;｡",
"(๑˃̶͈̀o˂̶͈́๑)",
"≧ω≦",
"(✧ ꒪◞౪◟꒪)",
"٩(^ᴗ^)۶",
"٩(๑꒦ິȏ꒦ິ๑)۶",
"٩(●˙▿˙●)۶…⋆ฺ",
"٩(๑ơలơ)۶♡",
"୧(﹒︠ᴗ﹒︡)୨",
"٩(ó｡ò۶ ♡)))♬",
"ε٩( ºωº )۶з",
"٩(๑òωó๑)۶",
"٩( ๑^ ꇴ^)۶",
"٩(๑˃́ꇴ˂̀๑)۶",
"٩(๑∂▿∂๑)۶♡",
"٩(♡ε♡ )۶",
"۹(ÒہÓ)۶",
"٩(⚙ȏ⚙)۶",
"٩(✿∂‿∂✿)۶",
"୧⍢⃝୨",
"⁽⁽٩(๑˃̶͈̀ ᗨ ˂̶͈́)۶⁾⁾",
"(୨৩́ಐ৩̀੧)",
"٩(;ʘ¿ʘ;)۶",
"=。:.ﾟ٩(๑&gt;ω&lt;๑)۶:.｡+ﾟ",
"٩(˘◊˘)۶",
"٩(*ゝڡゝ๑)۶♥",
"٩(｡θᗨθ｡)۶",
"٩(⚙ᴗ⚙)۶",
"୧(˃◡ु˂)୨",
"۹(˒௰˓)۶",
"٩(●ᴗ●)۶",
"♡〜٩( ˃́▿˂̀ )۶〜♡",
"٩(º౪º๑)۶",
"=。:.ﾟ٩(๑&gt;◊&lt;๑)۶:.｡+ﾟ",
"٩(๑❛ᴗ❛๑)۶",
"୧| ͡ᵔ ﹏ ͡ᵔ |୨",
"୧〳 ” ʘ̆ ᗜ ʘ̆ ” 〵୨",
"٩(๑❛ʚ❛๑)۶",
"٩(இ ⌓ இ๑)۶",
"୧| ” •̀ ل͜ •́ ” |୨",
"୧( , ＾ 〰 ＾ , )୨",
"٩| ര ‿ ര |╯",
"୧〳 ＾ ౪ ＾ 〵୨",
"୧( ˵ ° ~ ° ˵ )୨",
"୧། ☉ ౪ ☉ །୨",
"୧༼ ヘ ᗜ ヘ ༽୨",
"❣࿌ིྀ྇°˚࿅୧( ॑ധ ॑)୨࿅˳०࿌ིྀ྇",
"٩(◦`꒳´◦)۶",
"٩(๑˃̌ۿ˂̌๑)۶",
"˚₊*(ˊॢo̶̶̷̤◡ुo̴̶̷̤ˋॢ)*₊˚⁎",
"•ू(ᵒ̴̶̷ωᵒ̴̶̷*•ू) ​ )੭ु⁾",
"(❛ัॢᵕ❛ั ॢ)✩*ೃ.⋆",
"␟␏(ɲ˃ ˈ̫̮ ˂ɳ)␟␏ෆ",
"ෆ⃛(ٛ⌯ॢ˃ ɪ ˂ٛ⌯ॢ)",
"˚‧*♡ॢ˃̶̤̀◡˂̶̤́♡ॢ*‧˚",
"⁺✧.(˃̶ ॣ⌣ ॣ˂̶∗̀)ɞ⁾",
"₊*ˈ˚·(๑˃̶̡̢̥ ॣಐ ॣ˂̶̡̢̥๑)·˚ˈ*₊"]

meh = ["¯\_(ツ)_/¯",
"¯\(°_o)/¯",
"t(ツ)_/¯",
"┻━┻ ︵ ¯\ (ツ)/¯ ︵ ┻━┻",
"¯\_(⊙_ʖ⊙)_/¯",
"┐(´∀｀)┌",
"┐(´-｀)┌",
"└(・-・)┘",
"┗┐(*´Д｀*)┌┛",
"⋋〳 ᵕ _ʖ ᵕ 〵⋌",
"( ͡ _ ͡°)ﾉ⚲",
"o(ﾟДﾟ)っ",
"o(*´д`*)o",
"（ΩДΩ）",
"(O∆O)",
"ゞ◎Д◎ヾ",
"(⊃д⊂)",
"(ノдヽ)",
"(⊃‿⊂)",
"(/ω＼)",
"(／。＼)",
"（/｡＼)",
"（／．＼）",
"（／_＼）",
"(゜Д゜*)",
"(ﾟДﾟ;)",
"§;ﾟﾛﾟ§",
"(꒪ȏ꒪;)",
"(☼Д☼)",
"( ﾉД&#x60;)",
"(-@Д@)",
"(ﾟДﾟ；∬",
"⊂（゜Д゜⊂",
"⊃゜Д゜）⊃",
"（´皿｀；）",
"(＠O＠;)",
"( ⁰д⁰)",
") ゜o゜(",
"(ノ′Дヾ)",
"(　〇□〇）",
"(/;◇;)/",
"џ(ºДºџ)",
"ヽ(ﾟДﾟ)ﾉ",
"(」゜ロ゜)」",
"＼(●o○;)ノ",
"┗┐ヽ(′Д、`*)ﾉ┌┛",
"ヽ（・＿・；)ノ",
"ヾ(´･ ･｀｡)ノ”",
"ヽ(￣д￣;)ノ",
"ヽ（゜ロ゜；）ノ",
"ヾ(=ﾟ･ﾟ=)ﾉ",
"Σ(ﾟﾛﾟ｣)｣",
"ლ(´﹏`ლ)",
"╭(°A°`)╮",
"┌┤´ﾟДﾟ`├┐",
"ヾ( •́д•̀ ;)ﾉ",
"ヽ(*´Д｀*)ﾉ",
"ヽ(ﾟДﾟ)ﾉ",
"ヾ(◎o◎,,；)ﾉ",
"ヾ( ๑´д`๑)ﾂ",
"ヾ(*ㅿ*๑)ﾂ",
"ヾ(๑ ³ㅿ³)ﾉ",
"ヾ(((;ꈡ▱ꈡ;)))ﾉ",
"ʿʿ⁽⁽((⁰ⅈ⁰))⁾⁾ʾʾ",
"ヾ(ﾟдﾟ;)",
"ヽ(;´Д｀)ﾉ",
"ヾ(o´０ω０o)ﾉ",
"ヾ(o´０Д０o)ﾉ",
"&lt;(´・д・｀)ノ",
"ɭ ɿ (•᷄દ•᷅)",
"(ι´ Д｀)ﾉ",
"ヽ༼☯﹏☯༽ﾉ",
"੧║ ” ◔ Ĺ̯ ◔ ” ║و",
"ゞ( ͡°⍛ ͡°)ゞ",
"ヽ༼⊙_⊙༽ﾉ",
"ヾ(*’□’*)ｰ",
"ヾ(･ω･`；))ﾉ",
"&lt;(llﾟ◇ﾟll)&gt;",
"ヾ((；´･ω･)ﾉ",
"ヾ(･ω･`；)ﾉ",
"ヽ(*´□`)ﾉﾞ",
"ヾ(;ﾟ;Д;ﾟ;)ﾉﾞ",
"(*ﾉ´□`)ﾉ~",
"╰໒(⸝⸝⸝⚆Ĺ̯⚆⸝⸝⸝)७ノ",
"ヽ(‘ºل͟º)ノ",
"へ( ̿̿ o ̿̿ )╮",
"ԅ། , ◔ ﹏ ◔ , །ᓄ",
"ヽ(◕﹏◕)ﾉ",
"(○´･д･)ﾉ",
"(*′口`)ﾉ",
"ヽ(´･д･`)ﾉ",
"ヽ(･д･｀｡)ﾉ",
"ヽ(｡´･д･)ﾉ",
"ヾ(゜д゜)ノ",
"ヽ(*´□｀*)ッ",
"（┓゜Ａ゜）┓",
"ლ(ﾟдﾟლ)",
"ヽ(*゜∀゜*)ノ",
"ヾ(◕д◕❀)ﾂ",
"ヾ(❀◕д◕)ﾉ",
"（゜」∀」゜）",
"o|✿´・ェ・`|o",
"ヽ(▣﹏▣＼*≡*／▣﹏▣)ﾉ",
"/~＼o=(;ﾟﾛﾟ)=o/~＼",
".+:｡ヽUﾟДﾟUﾉﾟ.+:｡",
"ﾍ(ﾟ∀ﾟﾍ)ﾍ(ﾟ∀ﾟﾍ)ﾍ(ﾟ∀ﾟﾍ)",
"ଵ˛̼ଵ",
"⁎ۜ′̛˷˒′̛⌕",
"⋆ᶿ̵᷄ ˒̼ ᶿ̵᷅⋆"]

huh = ["ʕ ͠° ʖ̫ °͠ ʔ"]

glasses_animated = ["|","|•)","•_•)","( •_•)>⌐■-■","(⌐■_■)"]

emotions = {"excited":excited,"sad":sad,"meh":meh,"huh":huh}

def animate(an_emot_list,color=None):
    import os
    longest = 0
    for i in an_emot_list:
        if len(i) > longest:
            longest = len(i)
    import time
    for sym in an_emot_list:
        sym += (longest-len(sym))*" "
        sys.stdout.write(str(("\b"*longest)+"%s") % sym)
        sys.stdout.flush()
        time.sleep(.5)

def get_ran_emot(emotion):
    return random.sample(emotions[emotion],1)[0]

if __name__ == "__main__":
    print get_ran_emot("excited")
    print get_ran_emot("sad")
    print get_ran_emot("meh")
    print get_ran_emot("huh")
    