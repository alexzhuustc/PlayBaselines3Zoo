import torch

def check_gpu():
    # 检查 CUDA 是否可用
    if torch.cuda.is_available():
        print("CUDA is available! PyTorch can use GPU.")
        print(f"Number of available GPUs: {torch.cuda.device_count()}")
        print(f"Current GPU: {torch.cuda.get_device_name(torch.cuda.current_device())}")
    else:
        print("CUDA is not available. PyTorch will use CPU.")

if __name__ == "__main__":
    check_gpu()
