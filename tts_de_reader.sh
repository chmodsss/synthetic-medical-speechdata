counter=1
while read line;
do tts --text "$line" --model_name "tts_models/de/thorsten/tacotron2-DCA" --vocoder_name "vocoder_models/de/thorsten/wavegrad" --out_path `printf "wav/MT_%05g.wav" $counter`;
let counter=counter+1;
done < de_cimon_samples.txt
