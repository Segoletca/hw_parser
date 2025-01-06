import  logging 

def configure_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(module)40s:%(lineno)-3d %(levelname)-7s - %(message)s",
        # filename="legobase.log",
        # filemode="w",
    )
