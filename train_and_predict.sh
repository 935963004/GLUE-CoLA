CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python3 run_finetuning.py --data-dir ./data --model-name electra_large --hparams config.json
python3 to_result.py
