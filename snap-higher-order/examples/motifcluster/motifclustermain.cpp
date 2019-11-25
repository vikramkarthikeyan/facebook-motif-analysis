// motifcluster.cpp : Defines the entry point for the console application.
//
#include <map>
#include "stdafx.h"
#include "motifcluster.h"

int main(int argc, char* argv[]) {
  Env = TEnv(argc, argv, TNotify::StdNotify);
  Env.PrepArgs(TStr::Fmt("Motifs. build: %s, %s. Time: %s",
			 __TIME__, __DATE__, TExeTm::GetCurTm()));  
  TExeTm ExeTm;  
  Try
  const TStr graph_filename =
    Env.GetIfArgPrefixStr("-i:", "../as20graph.txt",
			  "Input directed graph file");
  const TStr node_filename =
    Env.GetIfArgPrefixStr("-n:", "../default.ngraph",
			  "Input node file");
  const TStr motif =
    Env.GetIfArgPrefixStr("-m:", "M4", "Motif type");

  TStr base_name = ("./" + graph_filename).RightOfLast('/').LeftOfLast('.');
  TStr default_output_filename = "output/" + base_name + "-" + motif + "-cluster.txt";
  const TStr output_filename =
    Env.GetIfArgPrefixStr("-o:", default_output_filename,
			  "Cluster output file");
  
  MotifType mt = MotifCluster::ParseMotifType(motif);
  PNGraph graph;
  if (graph_filename.GetFExt().GetLc() == ".ungraph") {
    TFIn FIn(graph_filename);
    graph = TSnap::ConvertGraph<PNGraph>(TUNGraph::Load(FIn), true);
  } else if (graph_filename.GetFExt().GetLc() == ".ngraph") {
    TFIn FIn(graph_filename);
    graph = TNGraph::Load(FIn);
  } else {
    graph = TSnap::LoadEdgeList<PNGraph>(graph_filename, 0, 1);
  }

  // Initialize Node_Gender map
  std::map<int, int> NodeGenderMap;

  // Get Node genders
  if (node_filename.GetFExt().GetLc() == ".nodelist") {
    TSnap::LoadNodeAttributes<PNGraph>(node_filename, NodeGenderMap, 0, 2);
  }

  TSweepCut sc;
  MotifCluster::GetMotifCluster(graph, mt, sc, NodeGenderMap);

  printf("Largest CC size: %d\n", sc.conn_components[sc.lcc_index].Len());
  printf("Cluster size: %d\n", sc.cluster.Len());
  printf("Motif conductance in largest CC: %f\n", sc.cond);
  printf("Eigenvalue: %f\n", sc.eig);

  MotifCluster::WriteSweepCutClusters(output_filename, sc);
  
  Catch
  printf("\nrun time: %s (%s)\n", ExeTm.GetTmStr(),
	 TSecTm::GetCurTm().GetTmStr().CStr());  
  return 0;
}
