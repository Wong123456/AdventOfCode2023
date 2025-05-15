f = open("day5.txt")

data = [str(line.strip()) for line in f]

def getSeedRanges(seeds):
    ls = [[int(seeds[i]), int(seeds[i]) + int(seeds[i + 1])] for i in range(len(seeds)) if i % 2 == 0]
    ls.sort(key= lambda x:x[0])
    return ls

seeds = seed_to_soil = soil_to_fert = fert_to_water = water_to_light = light_to_temp = temp_to_humid = humid_to_loc = []
for lineIdx in range(len(data)):
    lineStr = data[lineIdx]
    # print(lineStr)
    #get seeds
    if lineStr.startswith("seeds:"):
        seeds = getSeedRanges(lineStr.split(":")[1].split())
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

def getmapRule(mapData): #output: [[start, range, distance], [start, range, distace]] #[start1, end1, start2, end2]
    mapRule = []
    for data in mapData:
        source = int(data[1])
        destination = int(data[0])
        distance = destination - source
        ran = int(data[2]) - 1
        mapRule.append([source, source + ran, distance])
    mapRule.sort(key=lambda x:x[0])
    return mapRule

def delDupAndSort(ls: list):
    newLs = []
    for i in ls:
        if i not in newLs:
            newLs.append(i)
    newLs.sort(key=lambda x: x[0])
    return newLs

#overlapping of ranges can have 4 case: completely outside, partially inside, completely inside, completely inside, and partially inside other
def getMappedResult(seeds, mapRule):
    output = []
    for seedRange in seeds:
        sdStart, sdEnd = seedRange

        #if seed range completely out of map range, throw into output directly
        if sdEnd < mapRule[0][0] or sdStart > mapRule[len(mapRule) - 1][1]:
            output.append(seedRange)
            continue

        for mapRanIdx in range(len(mapRule)):
            currStart, currEnd, currDiff = map(int, mapRule[mapRanIdx])
            # print(sdStart, sdEnd, currStart, currEnd)
            prevStart = prevEnd = nextStart = nextEnd = None
            if -1 < mapRanIdx - 1: prevStart, prevEnd, prevDiff = map(int, mapRule[mapRanIdx - 1])
            if mapRanIdx + 1 < len(mapRule): nextStart, nextEnd, nextDiff = map(int, mapRule[mapRanIdx + 1])

            #completely outside, in between map range, throw into output directly
            if sdStart > currEnd:
                if nextStart is not None and nextEnd is not None:
                    if sdEnd < nextStart:
                        output.append(seedRange)
                # print("completely outside")

            #completely inside
            if sdStart >= currStart and sdEnd <= currEnd:
                # print("inside")
                output.append([sdStart + currDiff, sdEnd + currDiff])
                #direct translate entire seed range

            #overlap at front
            if currStart <=sdEnd <= currEnd and sdStart < currStart:
                #overlap at front and range before
                output.append([currStart + currDiff, sdEnd + currDiff])
                if prevStart is not None and prevEnd is not None: 
                    if sdStart <= prevEnd and not(prevEnd == currStart - 1):
                        # print("inside current and prev")
                        output.append([prevEnd + 1, currStart - 1])
                else: output.append([sdStart, currStart - 1])
                # print("pass front")

            #overlap at back
            if currStart <= sdStart <= currEnd and sdEnd > currEnd:
                # overlap at back and range after
                output.append([sdStart + currDiff, currEnd + currDiff])
                if nextStart is not None and nextEnd is not None:
                    if sdEnd >= nextStart and not(currEnd == nextStart - 1):
                        # print("inside curr and next")
                        output.append([currEnd + 1, nextStart - 1])
                else: 
                    output.append([currEnd + 1, sdEnd])

                # print("pass back")

            #fully overlap and extend front and back
            if sdStart < currStart and sdEnd > currEnd:
                # print("pass front and back")
                output.append([currStart + currDiff, currEnd + currDiff])

        # print("__________________________________________________________")
    return delDupAndSort(output)
                

soil_mr = getmapRule(seed_to_soil)
fert_mr = getmapRule(soil_to_fert)
water_mr = getmapRule(fert_to_water)
light_mr = getmapRule(water_to_light)
temp_mr = getmapRule(light_to_temp)
humid_mr = getmapRule(temp_to_humid)
loc_mr = getmapRule(humid_to_loc)

soil = getMappedResult(seeds, soil_mr)
fert = getMappedResult(soil, fert_mr)
water = getMappedResult(fert, water_mr)
light = getMappedResult(water, light_mr)
temp = getMappedResult(light, temp_mr)
humid = getMappedResult(temp, humid_mr)
loc = getMappedResult(humid, loc_mr)

print(loc[0][0])