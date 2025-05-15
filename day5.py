f = open("test.txt")

data = [str(line.strip()) for line in f]

seeds = seed_to_soil = soil_to_fert = fert_to_water = water_to_light = light_to_temp = temp_to_humid = humid_to_loc = []
for lineIdx in range(len(data)):
    lineStr = data[lineIdx]
    # print(lineStr)
    #get seeds
    if lineStr.startswith("seeds:"):
        seeds = lineStr.split(":")[1].split()
    #get seed to soil data
    if lineStr == "seed-to-soil map:":
        seed_to_soil = []
        stsIdx = lineIdx + 1
        while(not data[stsIdx] == ""):
            seed_to_soil.append(data[stsIdx].split())
            stsIdx += 1
        # print(seed_to_soil)
    if lineStr == "soil-to-fertilizer map:":
        soil_to_fert = []
        stfIdx = lineIdx + 1
        while(not data[stfIdx] == ""):
            soil_to_fert.append(data[stfIdx].split())
            stfIdx += 1
    if lineStr == "fertilizer-to-water map:":
        fert_to_water = []
        ftwIdx = lineIdx + 1
        while(not data[ftwIdx] == ""):
            fert_to_water.append(data[ftwIdx].split())
            ftwIdx += 1
    if lineStr == "water-to-light map:":
        water_to_light = []
        wtlIdx = lineIdx + 1
        while(not data[wtlIdx] == ""):
            water_to_light.append(data[wtlIdx].split())
            wtlIdx += 1
    if lineStr == "light-to-temperature map:":
        light_to_temp = []
        lttIdx = lineIdx + 1
        while(not data[lttIdx] == ""):
            light_to_temp.append(data[lttIdx].split())
            lttIdx += 1
    if lineStr == "temperature-to-humidity map:":
        temp_to_humid = []
        tthIdx = lineIdx + 1
        while(not data[tthIdx] == ""):
            temp_to_humid.append(data[tthIdx].split())
            tthIdx += 1
    if lineStr == "humidity-to-location map:":
        humid_to_loc = []
        htlIdx = lineIdx + 1
        while(htlIdx in range(len(data)) and not data[htlIdx] == ""):
            humid_to_loc.append(data[htlIdx].split())
            htlIdx += 1


def map(inputs, mapData):
    outputs = []
    for input in inputs:
        input = output = int(input)
        for data in mapData:
            source = int(data[1])
            destination = int(data[0])
            distance = destination - source
            ran = int(data[2]) - 1
            if source <= input <= source + ran:
                # print(source, destination, distance, input)
                # steps = input - source #step from the starting range to the seed
                # output = destination + steps
                output = input + distance
        outputs.append(output)
    return outputs

soil = map(seeds, seed_to_soil)
fert = map(soil, soil_to_fert)
water = map(fert, fert_to_water)
light = map(water, water_to_light)
temp = map(light, light_to_temp)
humid = map(temp, temp_to_humid)
loc = map(humid, humid_to_loc)
print(min(loc))

