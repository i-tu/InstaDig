let fileCount=1000
let dirNum=1

for f in *
do
[ -d $f ] && continue
[ $fileCount -eq 1000 ] && {
dir=$(printf "%03d", $dirNum)
mkdir $dir
let dirNum=$dirNum+1
let fileCount=0
}

mv $f $dir
let fileCount=$fileCount+1
done
