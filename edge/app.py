from pipelines.infer_pipeline import InferPipeline

def main():
    pipeline = InferPipeline(
        system_cfg="configs/system.yaml",
        camera_cfg="configs/camera.yaml",
        model_cfg="configs/model.yaml",
        counter_cfg="configs/counter.yaml",
    )
    pipeline.run()

if __name__ == "__main__":
    main()
