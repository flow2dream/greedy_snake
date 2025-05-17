import json
from utils.Block import Block

class World:
    def __init__(self, world_path, width, height):
        self.world = self.get_world(world_path)
        self.block_width = width / self.world["width"]
        self.block_height = height / self.world["height"]
        self.blocks = []
        self._init_blocks()
    
    def _init_blocks(self):
        for h in range(self.world["height"]):
            row_blocks = []
            for w in range(self.world["width"]):
                row_blocks.append(Block(w*self.block_width, h*self.block_height, self.block_width, self.block_height, self.world["blocks"][h][w]))
            self.blocks.append(row_blocks)

    def get_block_width(self):
        return self.block_width
    
    def get_block_height(self):
        return self.block_height
    
    def get_height(self):
        return self.world["height"]
    
    def get_width(self):
        return self.world["width"]

    def get_world(self, world_path):
        with open(world_path, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def get_block(self, x, y) -> Block:
        return self.blocks[y][x]
