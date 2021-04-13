counter=1
while read line;
do tts --text "$line" --model_name "tts_models/en/ljspeech/tacotron2-DCA" --vocoder_name "vocoder_models/en/ljspeech/multiband-melgan" --out_path `printf "wav/MT_%05g.wav" $counter`;
let counter=counter+1;
done < mtsamples_new.txt