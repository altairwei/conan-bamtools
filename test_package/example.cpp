#include <iostream>
#include "BamTools/api/BamMultiReader.h"
#include "BamTools/api/BamWriter.h"

using namespace std;
using namespace BamTools;

int main(int argc, char *argv[]) {
    string outputFilename = "merged.bam";
    vector<string> inputFilenames;
    for (int i = 1; i < argc; ++i) 
        inputFilenames.push_back(argv[i]); 

    // provide some input & output filenames
    // attempt to open our BamMultiReader
    BamMultiReader reader;
    if ( !reader.Open(inputFilenames) ) {
        cerr << "Could not open input BAM files." << endl;
        return 1;
    }
    // retrieve 'metadata' from BAM files, these are required by BamWriter
    const SamHeader header = reader.GetHeader();
    const RefVector references = reader.GetReferenceData();
    // attempt to open our BamWriter
    BamWriter writer;
    if ( !writer.Open(outputFilename, header, references) ) {
        cerr << "Could not open output BAM file" << endl;
        return 1;
    }
    // iterate through all alignments, only keeping ones with high map quality
    BamAlignment al;
    while ( reader.GetNextAlignmentCore(al) ) {
        writer.SaveAlignment(al);
    }
    // close the reader & writer
    reader.Close();
    writer.Close();
}
