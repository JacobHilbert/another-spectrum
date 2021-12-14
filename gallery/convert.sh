cd pdf
for file in *.pdf; do pdftoppm -png $file > $file.png; done
mv ./*.pdf.* ..
cd ..
(echo '# Gallery'; for file in *.png; do echo '![]('$file')'; done) > README.md
