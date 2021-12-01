wave = ParametricPlot3D[{
       {t , 0, -a Cos[t]},
       {t , a Cos[t], 0}
    }, {t, -0.3, 3 Pi}, {a, 0, 1.2},
    Mesh -> None, Axes -> False, Boxed -> False
    PlotRange -> {{-0.3, 3 Pi}, {-1.5, 1.5}, {-1.5, 1.5}},
    PlotStyle -> Opacity[0.5], PlotPoints -> 25
]

Ecolor = RGBColor["#f1820f"];
Bcolor = RGBColor["#1a2d52"];
Scolor = RGBColor["#8a141b"];

Etext = Style["Overscript[E, \[RightVector]]",\[CapitalEpsilon]color,20];
Btext = Style["Overscript[B, \[RightVector]]",\[CapitalBeta]color,20];
Stext = Style["Overscript[S, \[RightVector]]",Scolor,20];
phitext = Style["Overscript[\[Phi], ^]",Black,20];
thetatext = Style["Overscript[\[Theta], ^]",Black,20];
rtext = Style["Overscript[r, ^]",Black,30];
sigmatext = Style["\[PartialD]\[CapitalSigma]",Purple,30];

Show[
    wave,
    Graphics3D[{
        Thick,
        Bcolor, Arrow[{{0, 0, 0}, {0, 1.2, 0}}], Text[Btext, {0, 1.4, 0.0}],
        Ecolor, Arrow[{{0, 0, 0}, {0, 0, -1.2}}], Text[Etext, {0, -0, -1.4}],
        Scolor, Arrow[{{0, 0, 0}, {2.7, 0, 0}}], Text[Stext, {1.3, 0, 0.3}],
        White, Opacity[0.5], Sphere[{Pi/2, 0, 0}, 1.5 Pi],
        Black, Opacity[1],
          Arrow[{{2.01 Pi, 0, 0}, {2.01 Pi, 1, 0}}], Text[phitext, {2.01 Pi, 1.3, 0}],
          Arrow[{{2.01 Pi, 0, 0}, {2.01 Pi, 0, -1}}], Text[thetatext, {2.01 Pi, 0, -1.3}],
          Arrow[{{2.01 Pi, 0, 0}, {2.01 Pi + 1, 0, 0}}], Text[rtext, {2.01 Pi + 1.2, -0.1, 0.1}],
          Text[sigmatext, {2 Pi + 0.5, 0, 1}]
   }]
]