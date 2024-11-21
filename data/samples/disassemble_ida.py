import idaapi
import idautils
import idc

def write_instructions_to_file(output_file):
    with open(output_file, "w") as f:
        # Iterate through each segment
        for seg_ea in idautils.Segments():
            seg_name = idc.get_segm_name(seg_ea)
            f.write(f"Segment: {seg_name}\n")
            f.write(f"{'-'*40}\n")

            # Iterate through each instruction in the segment
            for head in idautils.Heads(seg_ea, idc.get_segm_end(seg_ea)):
                if idc.is_code(idc.get_full_flags(head)):
                    # Get the disassembled instruction
                    disasm_line = idc.generate_disasm_line(head, 0)
                    # Get the address of the instruction
                    address = f"{head:08X}"
                    f.write(f"{address}: {disasm_line}\n")

            f.write("\n")

def main():
    # Path to output file
    output_file = "output_instructions_temp.txt"

    print(f"Writing instructions to {output_file}...")
    write_instructions_to_file(output_file)
    print("Done!")

    # Exit IDA
    idaapi.qexit(0)

if __name__ == "__main__":
    main()