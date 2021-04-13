while read line;
do tts --text "$line" --model_name "tts_models/en/ljspeech/tacotron2-DCA" --vocoder_name "vocoder_models/en/ljspeech/mulitband-melgan" --out_path wav;
done < mtsamples_new.txt
