d = 2.2;
light = RGBColor[0.9, 0.2, 0.2];
green = RGBColor[0, 0.66, 0.33];
blue = RGBColor[0, 0.5, 1];
dash = 0.005;
S[s_] := Style[s, 18]
g = Graphics[{
   Arrowheads[0.02],
   Circle[],
   Yellow, Disk[{0, 0}, 0.1],
   blue, Disk[{Cos[80 \[Degree]], Sin[80 \[Degree]]}, 0.05],
   green, Disk[{Cos[250 \[Degree]], Sin[250 \[Degree]]}, 0.05],
   
   
   light,
   Dashing[dash],
   Line[{{Cos[250 \[Degree]], 
      Sin[250 \[Degree]]}, {Cos[250 \[Degree]], Sin[80 \[Degree]]}}],
   Text[S["\[CapitalDelta]"], {-0.5, 0}],
   Dashing[{}],
   Arrow[{{Cos[250 \[Degree]], 1.6}, {Cos[250 \[Degree]], 1}}],
   Arrow[{{Cos[80 \[Degree]], 1.6}, {Cos[80 \[Degree]], 1}}],
   Text[Style["Incoming light", 12], {0.5, 1.5}],
   
   Black,
   Circle[{d, 0}, 1],
   Yellow, Disk[{d, 0}, 0.1],
   RGBColor[0, 0.5, 1], 
   Disk[{Cos[80 \[Degree]] + d, Sin[80 \[Degree]]}, 0.05],
   Arrow[{{Cos[80 \[Degree]] + d, 
      Sin[80 \[Degree]]}, {Cos[80 \[Degree]] + d, 
      Sin[80 \[Degree]] + .3}}],
   Dashing[dash],
   Arrow[{{0 + d, 0}, {0 + d, Sin[80 \[Degree]]}}],
   Dashing[{}],
   
   RGBColor[0, 0.66, 0.33], 
   Disk[{Cos[250 \[Degree]] + d, Sin[250 \[Degree]]}, 0.05],
   Arrow[{{Cos[250 \[Degree]] + d, 
      Sin[250 \[Degree]]}, {Cos[250 \[Degree]] + d, 
      Sin[250 \[Degree]] + .3}}],
   Dashing[dash],
   Arrow[{{0 + d, 0}, {0 + d, Sin[250 \[Degree]]}}],
   Dashing[{}],
   
   Black,
   Arrow[{{0 + d, 0}, {Cos[80 \[Degree]] + d, Sin[80 \[Degree]]}}],
   Arrow[{{0 + d, 0}, {Cos[250 \[Degree]] + d, Sin[250 \[Degree]]}}],
   
   light,
   Arrow[{{Cos[250 \[Degree]] + d, 1.6}, {Cos[250 \[Degree]] + d, 
      Sin[250 \[Degree]] + 0.3}}],
   Arrow[{{Cos[80 \[Degree]] + d, 1.6}, {Cos[80 \[Degree]] + d, 1.3}}],
   Arrow[{{0 + d, 1.6}, {0 + d, 1}}],
   Text[Style["Incoming light", 12], {0.5 + d, 1.5}],
   
   green,
   Text[S["\!\(\*OverscriptBox[\(n\), \(^\)]\)"], {1.734, -0.7361}],
   Text[S[
     "\!\(\*OverscriptBox[\(r\), \(\[RightVector]\)]\)"], {2.001, \
-0.3325}],
   Text[S[
     "(\!\(\*OverscriptBox[\(n\), \
\(^\)]\)\[CenterDot]\!\(\*OverscriptBox[\(r\), \(\[RightVector]\)]\))\
\!\(\*OverscriptBox[\(r\), \(^\)]\)"], {2.388, -0.5031}],
   
   blue,
   Text[S["\!\(\*OverscriptBox[\(n\), \(^\)]\)"], {2.483, 1.119}],
   Text[S["\!\(\*OverscriptBox[\(r\), \(\[RightVector]\)]\)"], {2.408,
      0.4454}],
   Text[S[
     "(\!\(\*OverscriptBox[\(n\), \
\(^\)]\)\[CenterDot]\!\(\*OverscriptBox[\(r\), \(\[RightVector]\)]\))\
\!\(\*OverscriptBox[\(r\), \(^\)]\)"], {2.07, 0.5619}],
   
   Black,
   Text[S["a)"], {-1, 1}],
   Text[S["b)"], {-1 + d, 1}]
   }, ImageSize -> 800]