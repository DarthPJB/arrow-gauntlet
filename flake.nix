{
  inputs =
  {
    cqdev.url = "github:marcus7070/cq-flake";
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = { cqdev, self, nixpkgs }:
  let
    pkgs = nixpkgs.legacyPackages."x86_64-linux";
    defaultFileForCQ = "./source/casing.py";
    previewScriptName = "PreviewGeometary.sh";
  in
  {
    # Fast preview for current configuration
    apps."x86_64-linux".PreviewGeometary =
    let
      preview_script = pkgs.writeShellApplication
      {
        name = previewScriptName;
        runtimeInputs =
        [
          # Marcus cq-dev flake used to bring in the CQ enviroment
          cqdev.outputs.packages."x86_64-linux".cadquery-env
          # FastSTL for preview
          pkgs.fstl
        ];
        text = ''
          python full_model_generation.py
          for filename in output/*.stl; do
            fstl "$filename" &
          done
        '';
      };
    in
    {
      type = "app";
      program = "${preview_script}/bin/${previewScriptName}";
    };


    # devshell for quick development
    devShell."x86_64-linux" = pkgs.mkShell
    {
      buildInputs =
      [
        # Marcus cq-dev flake used to bring in the CQ enviroment
        cqdev.outputs.packages."x86_64-linux".cadquery-env
        # Marcus cq flake also provides Cadquery editor
        cqdev.outputs.packages."x86_64-linux".cq-editor
        # FastSTL viewer to view resulting STL files
        pkgs.fstl
        # viu for terminal-image viewing behaviour
        pkgs.viu
        # Inkscape for the inkview package (fast SVG viewer)
        pkgs.inkscape
        # atom and vim for effective code editing
        pkgs.atom pkgs.vim
        # figlet for attractive messages
        pkgs.figlet
      ];

    shellHook = ''
        figlet "Shell Active:"
        echo "starting editors"
        atom ./ --no-sandbox
        cq-editor ${defaultFileForCQ} &
        echo "to begin build sequence; run -"
        echo "nix run .#PreviewGeometary"
    '';
    };

    # generate final output stl files
    packages."x86_64-linux".cqgen = pkgs.stdenv.mkDerivation
    {
      name = "cqgen";
      src = self;
      buildInputs =
      [
        cqdev.outputs.packages."x86_64-linux".cadquery-env
      ];
      dontInstall = true;
      dontPatch = true;
      buildPhase = ''
        python full_model_generation.py
        mkdir -p $out
        mv output/*.stl $out/
      '';
    };

    defaultPackage."x86_64-linux" = self.packages."x86_64-linux".cqgen;
  };
}
