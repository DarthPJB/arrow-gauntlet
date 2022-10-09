# appending <current directory>/lib/ to python system path
#   This allows for importing local files outside of current WD
# sys.path.append(os.getcwd() + "/lib/");

# Load CQGI
import cadquery.cqgi as cqgi
import cadquery as cq
import os, sys
os.chdir('./source/')

model = cqgi.parse(open("casing.py").read());
build_result = model.build();
if build_result.success:
    count = 0;
    for result in build_result.results:
        cq.exporters.export(result.shape, '../output/casing_{i}.stl')
        count = count + 1;
else:
    print( "BUILD FAILED: " + str(build_result.exception) + "\n");
